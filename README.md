# Technical_data_assesment_incubyte
This repository conatins implementation of Incubyte Technical assesment for data Engineer

Concepts
Data processing
ETL
🔹Tools and Technology
Python
My sql Database
My sql Workbench
My sql connector-python
Datetime
Pandas
🔹Working
First Create Mysql database with specified Schema
database_connector.py python script, fetches database by establishing connection with MySQL server
Second Step is divided into further three parts:
Extract data from patients.txt file
Trasform date into specific format
For int data type convert null to 0 value
The data will be in panda-dataframe and inserted into database
The data of each country is retrieved in pandas dataframe and converted to pipe generated  .txt file
