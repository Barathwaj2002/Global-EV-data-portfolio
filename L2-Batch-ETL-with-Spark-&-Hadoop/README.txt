Overview:
This mini-project demonstrates loading Spark ETL outputs into Snowflake, a cloud data warehouse, for downstream BI analytics.

Steps
1. Exported Spark ETL outputs (`sales_by_year`, `sales_by_region`, `bev_phev_share`) as CSV.
2. Created Snowflake database, schema, and tables.
3. Used `COPY INTO` command to load data from cloud stage (Azure blob) into Snowflake tables.
4. Validated data with SQL queries.

Deliverables
- 'bev_phev_share.csv'
- 'sales_by_region.csv'
- 'sales_by_year.csv'
- `sql/tables_creation.sql`
- `sql/azure_integration.sql`
- `sql/stage_creation.sql`
- `sql/copy_into_tables.sql`
- Data now queryable inside Snowflake for BI tools (Power BI)
