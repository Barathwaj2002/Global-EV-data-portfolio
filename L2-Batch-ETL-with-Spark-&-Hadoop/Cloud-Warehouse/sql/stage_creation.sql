CREATE FILE FORMAT my_csv_format
  TYPE = 'CSV'
  FIELD_DELIMITER = ','
  SKIP_HEADER = 1
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  TRIM_SPACE = TRUE
  NULL_IF = ('NULL', 'null', '');

CREATE OR REPLACE STAGE azure_stage
  URL = 'azure://snowflakestorageaccount4.blob.core.windows.net/my-csv-container/'
  STORAGE_INTEGRATION = my_azure_integration
  FILE_FORMAT = my_csv_format;
  
CREATE OR REPLACE STAGE my_azure_stage
  URL = 'azure://snowflakestorageaccount4.blob.core.windows.net/my-csv-container/'
  CREDENTIALS = (
    AZURE_SAS_TOKEN = '?sv=2024-11-04&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2026-09-23T15:59:58Z&st=2025-09-23T07:44:58Z&spr=https&sig=cni%2BWiZPnAW8MPC0BrFYx4DS6y3ejdI2w%2FQ4lho2cAU%3D'
  )
  FILE_FORMAT = my_csv_format;


LIST @my_azure_stage;

GRANT USAGE ON DATABASE ETL_DATA TO ROLE ACCOUNTADMIN;
GRANT USAGE ON SCHEMA ETL_DATA.public TO ROLE ACCOUNTADMIN;