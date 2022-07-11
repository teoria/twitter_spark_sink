FROM apache/airflow:2.3.3

USER root

RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2
RUN apt-get update && \
apt-get install -y --no-install-recommends \
        openjdk-11-jre

# Prints installed java version, just for checking
RUN java --version

USER airflow
RUN pip install apache-airflow-providers-apache-spark==3.0.0
