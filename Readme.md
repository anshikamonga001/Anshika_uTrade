# Rate Limiter

## Algorithms
- Fixed Window
- Token Bucket

## Features
- Thread-safe
- Per client rate limiting
- Configurable via JSON
- HTTP interface

## Endpoints

POST /request?client_id=X
GET /stats

## Run

pip install flask requests

python main.py
python test_harness.py