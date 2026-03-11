import threading
import requests

URL = "http://localhost:5000/request"

clients = ["A", "B", "C", "D", "E"]

def send_requests(client):

    for _ in range(25):

        r = requests.post(
            URL,
            params={"client_id": client}
        )

        print(client, r.json())


threads = []

for c in clients:

    t = threading.Thread(
        target=send_requests,
        args=(c,)
    )

    threads.append(t)
    t.start()


for t in threads:
    t.join()