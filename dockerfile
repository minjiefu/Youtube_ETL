ARG AIRFLOW_VERSION=2.10.4
ARG PYTHON_VERSION=3.11

FROM apache/airflow:${AIRFLOW_VERSION}-python${PYTHON_VERSION}   
# Use official Airflow image as base image

ENV AIRFLOW_HOME=/opt/airflow

COPY requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt
