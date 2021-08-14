import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq-container'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello Workflow!')
print(" [x] Sent 'Hello World!'")
connection.close()
