CREATE STORAGE INTEGRATION my_azure_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'AZURE'
  ENABLED = TRUE
  AZURE_TENANT_ID = '441cd76b-3d73-4e64-94b4-934640d42f03'
  STORAGE_ALLOWED_LOCATIONS = ('azure://snowflakestorageaccount4.blob.core.windows.net/my-csv-container/');

desc storage integration my_azure_integration;
desc stage 
show integrations;