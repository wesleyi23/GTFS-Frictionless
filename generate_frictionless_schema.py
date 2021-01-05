#####
# Running this script produces a table schema for each .md file in tables_in_spec folder and a Frictionless data-package
#
# Results are output the tmp folder for review.
#####

import frictionless
import pandas
import os
import ast

def add_new_field(schema,
                  name,
                  frictionless_type,
                  format,
                  gtfs_required,
                  gtfs_type,
                  mark_down_description):

    if format == '':
        new_field = {
            'name': name,
            'type': frictionless_type,
            'description': mark_down_description,
            'gtfs_required': gtfs_required,
            'gtfs_type': gtfs_type
        }
    else:
        new_field = {
            'name': name,
            'type': frictionless_type,
            'format': format,
            'description': mark_down_description,
            'gtfs_required': gtfs_required,
            'gtfs_type': gtfs_type,
        }

    schema.add_field(new_field)
    return schema


def read_md_table(path):
    df = pandas.read_table(path, sep=r'\s*\|\s*', header=0, skipinitialspace=True, encoding='utf-8')
    df['Field Name'] = df['Field Name'].str.replace('`', '')
    df['Required'] = df['Required'].str.replace('*', '')
    df = df.iloc[1:]
    return df


def add_frictionless_field_types(df):
    frictionless_types = pandas.read_csv('lookup_tables/gtfs_types_to_frictionless_types.csv')
    df = df.merge(frictionless_types, on=['Type'], how='left')
    df = df.fillna('')
    return df


def get_md_table_path_from_file_name(gtfs_file_name):
    return 'tables_in_spec/' + gtfs_file_name.replace('.txt', '.md')


def create_spec(gtfs_file_name, constraints_in_schema=True):
    # Load constraint lookup tables
    type_based_constraints = pandas.read_csv('lookup_tables/type_based_constraints.csv')
    type_based_constraints = type_based_constraints[type_based_constraints["Constraint"].notnull()]

    constraints = pandas.read_csv('lookup_tables/constraints.csv')
    constraints = constraints[constraints["Constraint"].notnull()]
    constraints = constraints[constraints['Table'] == gtfs_file_name]

    foreign_keys = pandas.read_csv('lookup_tables/foreign_keys.csv')
    foreign_keys = foreign_keys[foreign_keys["Field"].notnull()]

    primary_keys = pandas.read_csv('lookup_tables/primary_keys.csv')
    primary_keys = primary_keys[primary_keys["Primary Key Value"].notnull()]

    # Load markdown tables
    path = get_md_table_path_from_file_name(gtfs_file_name)
    df = read_md_table(path)
    df = add_frictionless_field_types(df)
    schema = frictionless.Schema()

    # iterate through markdown tables and add fields
    for index, row in df.iterrows():
        schema = add_new_field(schema,
                               name=row['Field Name'],
                               frictionless_type=row['Frictionless Type'],
                               format=row['Format'],
                               gtfs_required=row['Required'],
                               gtfs_type=row['Type'],
                               mark_down_description=row['Description'])

        # add required constraints
        if row['Required'] == 'Required':
            schema.get_field(row['Field Name']).constraints['required'] = 'true'

        # add type based constraints
        if row['Type'] in list(type_based_constraints['Type']):
            for c_index, c_row in type_based_constraints[type_based_constraints['Type'] == row['Type']].iterrows():
                schema.get_field(row['Field Name']).constraints[c_row['Constraint']] = c_row['Value']

        #add enum constraints
        if constraints_in_schema:

            if row['Field Name'] in list(constraints['Field Name']):
                constraint_type = constraints.loc[constraints['Field Name'] == row['Field Name']]['Constraint'].item()
                constraint_value = constraints.loc[constraints['Field Name'] == row['Field Name']]['Value'].item()
                constraint_value = ast.literal_eval(str(constraint_value))
                schema.get_field(row['Field Name']).constraints[constraint_type] = constraint_value




    # add primary keys
    if gtfs_file_name in list(primary_keys['Table']):
        if '[' in primary_keys[primary_keys['Table'] == gtfs_file_name].iloc[0]['Primary Key Value']:
            schema.primary_key = ast.literal_eval(primary_keys[primary_keys['Table'] == gtfs_file_name].iloc[0]['Primary Key Value'])
        else:
            schema.primary_key = primary_keys[primary_keys['Table'] == gtfs_file_name].iloc[0]['Primary Key Value']

    # add foreign keys
        if gtfs_file_name in list(foreign_keys['Table']):
            for index, row in foreign_keys[foreign_keys['Table'] == gtfs_file_name].iterrows():
                schema.foreign_keys.append(
                    {"fields": [row['Field']],
                     "reference": {"resource": row['Reference'],
                                   "fields": row['Reference Field']}}
                )

    # TODO add testing and validation

    # write to json
    # schema.to_yaml("./tmp/" + gtfs_file_name.replace('.txt', '.yaml'))
    schema.to_json("./tmp/" + gtfs_file_name.replace('.txt', '.json'))


# For each file run create the table schema and package into a data package
package = frictionless.Package(name="GTFS-Frictionless")

files = os.listdir("tables_in_spec")

for i in files:
    j = i.replace('.md', '.txt')
    print(j)
    create_spec(j)
    schema = frictionless.Schema('./tmp/' + j.replace('.txt', '.json'))
    resource = frictionless.Resource(name=j,
                                     path="./" + j,
                                     schema=schema)
    package.add_resource(resource)

package.to_json("./tmp/data-package.json")