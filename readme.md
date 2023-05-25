Dont forget;

chmod +x mysql-start.sh

After run this command mysql-start.sh

docker exec -it mysql bash

mysql -u root -p

create database traindb;

GRANT ALL PRIVILEGES ON traindb.* TO 'train'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

exit

mysql -u traindb -D train -p
