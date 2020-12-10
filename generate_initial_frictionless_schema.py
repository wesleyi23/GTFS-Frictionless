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


def create_spec(gtfs_file_name, enum_constraints_in_schema=True):
    # Load constraint lookup tables
    type_based_constraints = pandas.read_csv('lookup_tables/type_based_constraints.csv')
    type_based_constraints = type_based_constraints[type_based_constraints["Constraint"].notnull()]

    enum_constraints = pandas.read_csv('lookup_tables/enum_constraints.csv')
    enum_constraints = enum_constraints[enum_constraints["Constraint"].notnull()]
    enum_constraints = enum_constraints[enum_constraints['Table'] == gtfs_file_name]

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
        if enum_constraints_in_schema:
            if row['Field Name'] in list(enum_constraints['Field Name']):
                for c_index, c_row in enum_constraints.iterrows():
                    schema.get_field(row['Field Name']).constraints['enum'] = ast.literal_eval(c_row['Value'])


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


    # schema.to_yaml("./tmp/" + gtfs_file_name.replace('.txt', '.yaml'))
    schema.to_json("./tmp/" + gtfs_file_name.replace('.txt', '.json'))



files = os.listdir("example_files")

for i in files:
    create_spec(i)

create_spec('attributions.txt')


