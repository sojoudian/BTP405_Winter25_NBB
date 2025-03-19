
## Test user registration
```bash
curl -X POST "http://127.0.0.1:5001/api/register" -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}'
```

## run the mongoDB without Python in container
```bash
docker run -d --name chatappDB -p 27017:27017 mongo:latest
```


## Run mongoDB and Python app using container:
```bash
docker network create chatapp_network
docker run -d --name chatappDB --network chatapp_network -p 27017:27017 mongo:latest
docker run -d --name my-backend --network chatapp_network my-backend
```