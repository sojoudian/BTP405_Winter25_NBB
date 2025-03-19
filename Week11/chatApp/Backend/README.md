
## Test user registration
```bash
curl -X POST "http://127.0.0.1:5001/api/register" -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}'
```

## run the mongoDB