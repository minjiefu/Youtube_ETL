# **Youtube API - ELT**

## **Goal** 

The aim of this project is to produce an ELT data pipeline using data engineering tools such as Python, Docker & Airflow. To make the pipeline more robust, best practices of unit & data quality testing and continuous integration/continuous deployment (CI-CD) are also implemented.

## **Dataset** 

As a data source, the Youtube API is used. The data of this project is pulled from a popular channel - 'MrBeast'.

## **Implementation**

This ELT project uses Airflow as an orchestration tool, packaged inside docker containers. The steps that make up the project are as follows:

1. Data is **extracted** using the Youtube API with Python scripts 
2. The data is initially **loaded** into a `staging schema` which is a dockerized PostgreSQL database
3. From there, a python script is used for data **transformations** where the data is then loaded into the `core schema` (also a dockerized PostgreSQL database)
4. Once the core schema is populated and both unit and data quality tests have been implemented, the data is then ready for analysis.

Three DAGs exist, triggered one after the other. The DAGs are as follows;

* *produce_json* - DAG to produce JSON file with raw data
* *update_db* - DAG to process JSON file and insert data into booth staging and core schemas
* *data_quality* - DAG to check the data quality on both layers in the database

## **Tools & Technologies**

* *Containerization* - **Docker**, **Docker-Compose**
* *Orchestration* - **Airflow**
* *Data Storage* - **Postgres**
* *Languages* - **Python, SQL**
* *Testing* - **SODA**, **pytest**
* *CI-CD* - **Github Actions**
