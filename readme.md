Dont forget;

chmod +x mysql-start.sh

After run this command mysql-start.sh

docker exec -it mysql-server bash

mysql -u root -p

create database traindb;

GRANT ALL PRIVILEGES ON traindb.* TO 'train'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

exit

mysql -u traindb -D train -p

uvicorn mainapp.main:app --host 0.0.0.0 --port 8002 --reload

https://raw.githubusercontent.com/erkansirin78/datasets/master/retail_db/customers.csv
