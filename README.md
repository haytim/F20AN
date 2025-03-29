## List of commands

### Starting

dcbuild


docker-compose up -d

### Running Scripts

docker exec -it user1-10.9.0.6 bash

curl http://10.9.0.5/ 



### Adam's Running Script

apt update -y

apt install python3

apt install git

git clone REPO

ls REPO

python filename.py


### Check if hosts are running

docker ps

### Create html files for nginx and caddy

sudo chown -R $USER:$USER ./nginx_site

sudo chown -R $USER:$USER ./caddy_site


chmod -R 755 ./nginx_site

echo "<h1>Hello Nginx</h1>" > ./nginx_site/index.html


chmod -R 755 ./caddy_site

echo "<h1>Hello Caddy</h1>" > ./caddy_site/index.html


