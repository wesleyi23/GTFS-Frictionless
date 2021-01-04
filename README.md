# GTFS-Frictionless

**UNDER DEVELOPMENT**

An effort to create a [Frictionless Schema](https://frictionlessdata.io/) for the GTFS specification. Frictionless is a 
set of patterns for describing data including Data Package (for datasets), Data Resource (for files) and Table Schema 
(for tables).

Running the python script [generate_frictionless_schema.py](generate_frictionless_schema.py)
will use a table driven approach to produce a [Frictionless Data Package Schema](https://specs.frictionlessdata.io/data-package/)
for the GTFS specification and [Frictionless Table Schemas](https://specs.frictionlessdata.io/table-schema/) for each 
file in a GTFS feed. 

Data from the GTFS specification has been copied from the markdown tables in the specification to a markdown file for each GTFS 
file. These may be found in the tables_in_spec folder and may be updated as the specification changes.

Look up tables for metadata, required by the Frictionless data standards, are in the lookup_tables folder.  You will find 
the following tables in that folder:

- [gtfs_types_to_frictionless_types.csv](lookup_tables/gtfs_types_to_frictionless_types.csv) - a crosswalk 
  of field types in the GTFS specification to their corresponding Frictionless field types
  
- [type_based_constraints.csv](lookup_tables/type_based_constraints.csv) - a table of constraints that apply based on
  the GTFS type.
  
- [constraints.csv](lookup_tables/constraints.csv) - a table of constraints that are applied to the frictionless schema 
  by GTFS table and field name

- [primary_keys.csv](lookup_tables/primary_keys.csv) - a table of primary keys in the GTFS specification. Note: It does
  not include conditional primary keys.
  
- [foreign_keys.csv](lookup_tables/foreign_keys.csv) - a table of foreign keys in the GTFS specification. 
  
Based on work by Stephen Gates: https://github.com/Stephen-Gates/GTFS
