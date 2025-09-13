FROM apache/superset:latest

ARG INSTANT_CLIENT_VERSION=21.13.0.0.0
ARG INSTANT_CLIENT_BASIC_PACKAGE=instantclient-basiclite-linux.x64-${INSTANT_CLIENT_VERSION}.zip
ARG INSTANT_CLIENT_SDK_PACKAGE=instantclient-sdk-linux.x64-${INSTANT_CLIENT_VERSION}.zip

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip \
    libaio1 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY ./instantclient_files/instantclient-basic-linux.arm64-23.8.0.25.04.zip /tmp/instantclient-basic.zip
COPY ./instantclient_files/instantclient-sdk-linux.arm64-23.8.0.25.04.zip /tmp/instantclient-sdk.zip

RUN mkdir -p /opt/oracle \
    && unzip -o /tmp/instantclient-basic.zip -d /opt/oracle \
    && unzip -o /tmp/instantclient-sdk.zip -d /opt/oracle \
    && rm /tmp/instantclient-basic.zip /tmp/instantclient-sdk.zip

RUN ORACLE_INSTANT_CLIENT_DIR=$(ls -d /opt/oracle/instantclient_*) \
    && ln -s ${ORACLE_INSTANT_CLIENT_DIR} /opt/oracle/instantclient_latest \
    && echo ${ORACLE_INSTANT_CLIENT_DIR} > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig

ENV TNS_ADMIN=/opt/oracle/instantclient_latest/network/admin
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_latest:$LD_LIBRARY_PATH
ENV PATH=/opt/oracle/instantclient_latest:$PATH

RUN pip install --no-cache-dir oracledb
USER superset