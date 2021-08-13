import pika
import sys
import time

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq-container'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_multi', exchange_type='direct')

message = ' '.join(sys.argv[1:]) or "info: Hello World from PUB1!"
while True:
    channel.basic_publish(exchange='logs_multi', routing_key='logs_from_pub1', body=message)
    print(" [x] Sent %r" % message)
    time.sleep(1)
connection.close()
