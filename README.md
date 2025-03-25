# Trusted URL Checker API

This API checks if a given URL is in a list of 4 million trusted URLs from the Tranco list.

## Features

- Fast URL lookup using in-memory set data structure
- URL normalization (removes protocols, www, trailing slashes)
- Simple REST API interface

## API Endpoints

### Check URL
```
POST /check-url
Content-Type: application/json

{
    "url": "example.com"
}
```

Response:
```json
{
    "url": "example.com",
    "is_trusted": true/false,
    "normalized_url": "example.com"
}
```

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API:
```bash
python main.py
```

The API will be available at http://localhost:8000 