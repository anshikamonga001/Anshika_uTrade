import json
import time
from flask import Flask, request
from algorithms.fixed_window import FixedWindowLimiter
from algorithms.token_bucket import TokenBucketLimiter

app = Flask(__name__)

with open("config.json") as f:
    config = json.load(f)

if config["algorithm"] == "fixed_window":
    limiter = FixedWindowLimiter(
        config["max_requests"],
        config["window_seconds"]
    )
else:
    limiter = TokenBucketLimiter(
        config["token_bucket"]["capacity"],
        config["token_bucket"]["refill_rate"]
    )

stats = {
    "total": 0,
    "allowed": 0,
    "rejected": 0
}


@app.route("/request", methods=["POST"])
def handle_request():

    client_id = request.args.get("client_id")
    result = limiter.allow_request(client_id)

    stats["total"] += 1

    if result:
        stats["allowed"] += 1
        status = "ALLOWED"
    else:
        stats["rejected"] += 1
        status = "RATE_LIMITED"

    print(time.time(), client_id, config["algorithm"], status)

    return {"result": status}


@app.route("/stats")
def get_stats():
    return stats


if __name__ == "__main__":
    app.run(threaded=True)