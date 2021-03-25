# Summary
 
A fictious company "Sparkify" is a music streaming start-up which has grown their user base and song database to the point where a cloud solution would better suit their needs. I have been tasked (as their Data Engineer) to build an ETL pipeline that extracts their data from an S3 bucket, stages the data in Redshift and then transforms the data into a set of dimensional tables for their analytics team.

### The process I performed was the following:

- Created an IAM user - attaching the correct Redshift security policies (Administrator access, S3Bucket Read-only)
- Create a Redshift cluster and utilising its Endpoint to access it programmatically 
- Creating SQL queries to:
    1. Drop existing tables
    2. Create the new tables
    3. Load the Staging tables
    4. Transform the tables into a set of dimensional tables in Redshift


# How to Run

1. Run `create_tables.py` to drop and create the tables
2. Run `etl.py` to load and insert the staging tables 


# Additional Files in Repository

- `dwh.cfg` sets up the configurations for AWS
- `test.ipynb` is to test whether the scripts `create_tables.py` and `etl.py` works
