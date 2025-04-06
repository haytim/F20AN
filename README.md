```
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

USE python3 benchmark.py <apache|nginx|caddy> output.txt <iterations>
  
done

### Code for implementing countermeasure

docker exec -it my-apache-app bash

apt update && apt install -y nano

nano /usr/local/apache2/conf/httpd.conf

Level 1 - No Additional Protection to KeepAlive Off

KeepAlive Off

Level 2 - Minimal

<IfModule reqtimeout_module>
    RequestReadTimeout header=30-40,MinRate=200
</IfModule>

KeepAlive Off

Level 3 - Moderate

<IfModule reqtimeout_module>
    RequestReadTimeout header=20-30,MinRate=400
</IfModule>

Level 4 - Strong

<IfModule reqtimeout_module>
    RequestReadTimeout header=10-20,MinRate=800
</IfModule>

KeepAlive Off

Level 5 - Aggresive

<IfModule reqtimeout_module>
    RequestReadTimeout header=5-10,MinRate=1600
</IfModule>

KeepAlive Off

### Keep Alive On Settings

MaxKeepAliveRequests 50

KeepAliveTimeout 2

### Restart Apache after changing config

apachectl restart
```
