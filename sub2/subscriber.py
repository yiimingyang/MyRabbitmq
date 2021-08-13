import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq-container'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_multi', exchange_type='direct')

#result = channel.queue_declare(queue='', exclusive=True)
#queue_name = result.method.queue

channel.queue_declare(queue='queue_pub1')

channel.queue_bind(exchange='logs_multi', queue='queue_pub1', routing_key = 'logs_from_pub1')
#channel.queue_bind(exchange='logs_multi', queue='queue_pub1', routing_key = 'logs_from_pub2')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body.decode())

channel.basic_consume(
    queue='queue_pub1', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
