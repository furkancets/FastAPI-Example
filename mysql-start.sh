docker run --name mysql-server -p 3306:3306 -v /opt/data:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=Ankara06 -e MYSQL_USER=train -e MYSQL_PASSWORD=Ankara06 -d mysql
