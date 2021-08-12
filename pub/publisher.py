import pika
import sys
import time

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq-container'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
while True:
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    time.sleep(1)
connection.close()
