CREATE KEYSPACE movielens WITH replication = {'class':'SimpleStrategy', 'replication_factor':'1'} AND durable_writes = true;
USE movielens;
CREATE TABLE users (user_id int, age int, gender text, occupation text, zip text, PRIMARY KEY (user_id));
DESCRIBE TABLE users;
