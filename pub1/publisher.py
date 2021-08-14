import pika
import sys
import time

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq-container'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_multi', exchange_type='direct')
channel.queue_declare(queue='queue_pub1')

channel.exchange_declare(exchange='logs_extra', exchange_type='direct')
channel.queue_declare(queue='queue_pub_extra')

message1 = ' '.join(sys.argv[1:]) or "info: Hello World from PUB1!"
message2 = "info: message from Extra!"
while True:
    channel.basic_publish(exchange='logs_multi', routing_key='logs_from_pub1', body=message1)
    channel.basic_publish(exchange='logs_extra', routing_key='logs_from_extra', body=message2)
    print(" [x] Sent %r" % message1)
    print(" [x] Sent %r" % message2)
    time.sleep(1)
connection.close()
