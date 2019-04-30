#!/bin/bash

HOME_PATH="/home/maria_dev/"
DOWNLOAD_URL="http://archive.apache.org/dist/drill/drill-1.12.0/apache-drill-1.12.0.tar.gz"
DRILL_TAR="apache-drill-1.12.0.tar.gz"

wget -nc $DOWNLOAD_URL -P $HOME_PATH

tar -xvf ${HOME_PATH}${DRILL_TAR} --directory $HOME_PATH

if grep -R "http.port:" ${HOME_PATH}apache-drill-1.12.0/conf/drill-override.conf; then
  echo "Drill port already configured";
else
  echo "Overriding current http.port setting to 8765"
  sed -i 's/}/  http.port: "8765"\n}/g' ${HOME_PATH}apache-drill-1.12.0/conf/drill-override.conf;
fi

${HOME_PATH}apache-drill-1.12.0/bin/drillbit.sh start

# still need to enable MongoDB storage via CLI
