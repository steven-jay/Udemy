#!/bin/bash

MONGO_DIR="/var/lib/ambari-server/resources/stacks/HDP/2.6/services/mongo-ambari"
export SERVICE=MONGODB
export PASSWORD=hadoopadmin
export AMBARI_HOST="localhost"
export CLUSTER="Sandbox"
export SPARK_MAJOR_VERSION=2
HOME_PATH="/home/maria_dev/"

if [ ! -d $MONGO_DIR ]; then
  cd /var/lib/ambari-server/resources/stacks/HDP/2.6/services
  git clone https://github.com/nikunjness/mongo-ambari.git
  service ambari-server restart
fi

pip install pymongo
# currently appears the service needs to be added via Ambari UI. May need to stop script and add it manually, then start service

curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Start $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "STARTED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.3.1 ${HOME_PATH}MongoSpark.py
