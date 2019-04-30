 #!/bin/bash

echo 'Prepping container...'

USER="root"
IP="0.0.0.0"
HADOOP_PATH="/Users/stephenjusuf/Development/Udemy/Hadoop/"
CONTAINER="sandbox-hdp"
REPO_PATH="/etc/yum.repos.d/"
HOME_PATH="/home/maria_dev/"

echo "Generating key pair..."
if [ ! -f /Users/stephenjusuf/.ssh/id_rsa ]; then
  ssh-keygen -t rsa
  ssh-copy-id $USER@$IP
else
  echo "Key already exists"
  ssh-copy-id $USER@$IP
fi

# copy DataStax repo information to container
echo "Copying DataStax Repo to container\n"
docker cp "${HADOOP_PATH}datastax.repo" "${CONTAINER}:/etc/yum.repos.d/datastax.repo"
docker cp "${HADOOP_PATH}setup_cassandra_table.cql" "${CONTAINER}:${HOME_PATH}setup_cassandra_table.cql"
docker cp "${HADOOP_PATH}setup_mysql.sql" "${CONTAINER}:${HOME_PATH}setup_mysql.sql"
docker cp "${HADOOP_PATH}create_movielens_table.sql" "${CONTAINER}:${HOME_PATH}create_movielens_table.sql"

#SCRIPTS=("download_files.sh" "install_mysql.sh" "install_cassandra.sh" "install_mongodb.sh" "install_drill.sh")
SCRIPTS=("install_drill.sh")
for i in "${SCRIPTS[@]}"; do
  echo "Running ${i}"
  echo ""
  ssh $USER@$IP 'bash -s' < ./$i
done

echo 'Container is ready'
