#!/bin/bash

hadoop fs -mkdir ./ml-100k;

dataURL="http://media.sundog-soft.com/hadoop/ml-100k/"
scriptURL="http://media.sundog-soft.com/hadoop/"
containerFilePath="/home/maria_dev/"
hdfsFilePath="/user/maria_dev/ml-100k/"

echo "Check if files exists: ${containerFilePath}u.data"

if [ ! -f "${containerFilePath}u.data" ]; then
  # download data files and copy to HDFS
  echo 'Getting files...'
  for FILE in "u.data" "u.item" "u.user"; do
    echo "Downloading file from $dataURL${FILE}"
    wget -nc $dataURL${FILE} -P $containerFilePath
    hadoop fs -copyFromLocal $containerFilePath${FILE} $hdfsFilePath${FILE}
  done

  # download script files and store in maria_dev home directory
  for FILE in "CassandraSpark.py" "MongoSpark.py"; do
    echo "Downloading file from $scriptURL${FILE}"
    wget -nc $scriptURL${FILE} -P $containerFilePath
  done
else
  echo 'Files already exist'
fi

hadoop fs -ls ./ml-100k
