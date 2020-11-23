# Simple API
Runs on !
- Python3
- Flask
- Docker

Installing Docker and Docker-Compose
```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
rm -f get-docker.sh

sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Run the API using Docker:
```sh
cd /path/to/code/directory
docker-compose up -d
```


### Sample response:
```sh
curl http://localhost/ ; echo
{ "type": "success", "value": { "id": 537, "joke": "Each hair in Rodrick Pfannerstill'ss beard contributes to make the world's largest DDOS.", "categories": ["nerdy"] } }
```

### Run test case:
```sh
coverage report api/test_random_url.py
```