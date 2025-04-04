## List of commands

### Starting

dcbuild


docker-compose up -d

### Enter Host Terminal

docker exec -it my-apache-app bash

docker exec -it seed-attacker bash

docker exec -it seed-attacker2 bash

docker exec -it user1-10.9.0.6 bash

### Adam's Running Script

apt update -y

apt install python3

apt install git

git clone https://github.com/haytim/F20AN.git

ls F20AN

cd F20AN

cd scripts

python3 slowloris.py


### Check if hosts are running

docker ps

### Run Connection Benchmark

curl -o /dev/null -s -w "Time Total: %{time_total}\\n" http://10.9.0.5


or


while true; do

  echo -n "$(date) - " >> curl_log.txt
  
  curl -o /dev/null -s -w "Time Total: %{time_total}\\n" http://10.9.0.5 >> curl_log.txt
  
  sleep 5
  
done

### Code for implementing countermeasure

docker exec -it my-apache-app bash

apt update && apt install -y nano

nano /usr/local/apache2/conf/httpd.conf


\<IfModule reqtimeout_module\>
  \
    RequestReadTimeout header=10-20,MinRate=500
    
\</IfModule\>

KeepAlive Off

# Keep Alive On Settings

MaxKeepAliveRequests 50

KeepAliveTimeout 2

### Restart Apache after changing config

apachectl restart
