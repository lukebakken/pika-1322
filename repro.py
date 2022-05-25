import pika
from pika.exchange_type import ExchangeType

import time

exch = "pika-1322"
credentials = pika.PlainCredentials("guest", "guest")
params = pika.ConnectionParameters("shostakovich", 5672, "/", credentials, heartbeat=60)
conn = pika.BlockingConnection(params)
chan = conn.channel()
chan.exchange_declare(
    exchange=exch, exchange_type=ExchangeType.direct, durable=False, auto_delete=True
)

while True:
    time.sleep(5)
    print("publishing...")
    chan.basic_publish(exchange=exch, routing_key="foobar", body="bazbat")
