#!/bin/bash

echo 'Installing Cassandra now...'

yum -y update

if [ -f /etc/yum.repos.d/datastax.repo ]; then
  yum -y install dsc30
else
  echo "Cannot locate DataStax Repo"
fi

yum -y install python-pip
pip install cqlsh

service cassandra start
sleep 10
cqlsh --cqlversion="3.4.0" -f /home/maria_dev/setup_cassandra_table.cql

export SPARK_MAJOR_VERSION=2
# need to make sure using correct DataStax package with Scala and Spark version.
# can check Spark using spark-submit --version
spark-submit --packages datastax:spark-cassandra-connector:2.3.1-s_2.11 /home/maria_dev/CassandraSpark.py

cqlsh --cqlversion="3.4.0" -e "USE movielens; SELECT * FROM users LIMIT 10;"
