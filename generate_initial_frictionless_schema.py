import frictionless
import pandas
import os


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


def add_frictionless_field_types(df, gtfs_file_name):
    frictionless_types = pandas.read_csv('lookup_tables/gtfs_types_to_frictionless_types.csv')
    df = df.merge(frictionless_types, on=['Type'], how='left')
    df = df.fillna('')
    return df


def get_md_table_path_from_file_name(gtfs_file_name):
    return 'tables_in_spec/' + gtfs_file_name.replace('.txt', '.md')


def create_spec(gtfs_file_name):
    path = get_md_table_path_from_file_name(gtfs_file_name)
    df = read_md_table(path)
    df = add_frictionless_field_types(df, gtfs_file_name)
    schema = frictionless.Schema()

    for index, row in df.iterrows():
        schema = add_new_field(schema,
                               name=row['Field Name'],
                               frictionless_type=row['Frictionless Type'],
                               format=row['Format'],
                               gtfs_required=row['Required'],
                               gtfs_type=row['Type'],
                               mark_down_description=row['Description'])


    # schema.to_yaml("./tmp/" + gtfs_file_name.replace('.txt', '.yaml'))
    schema.to_json("./tmp/" + gtfs_file_name.replace('.txt', '.json'))


files = os.listdir("example_files")

for i in files:
    create_spec(i)

create_spec('attributions.txt')


