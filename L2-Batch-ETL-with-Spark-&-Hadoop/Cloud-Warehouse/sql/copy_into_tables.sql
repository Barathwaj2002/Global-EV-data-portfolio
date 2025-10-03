copy into sales_by_region from @my_azure_stage/sales_by_region.csv file_format = (format_name = my_csv_format) on_error = 'continue';

select * from sales_by_region;

copy into sales_by_year from @my_azure_stage/sales_by_year.csv file_format = (format_name = my_csv_format) on_error = 'continue';

select * from sales_by_year;

copy into bev_phev_2023 from @my_azure_stage/sales_by_region.csv file_format = (format_name = my_csv_format) on_error = 'continue';

select * from bev_phev_2023;

drop table bev_phev_2023;

