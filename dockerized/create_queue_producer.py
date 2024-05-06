import time
from constants import (URI,QUEUE_PRODUCER, EXCHANGE_QUEUE, ROUTING_KEY)
import pika


try:
    parameters = pika.URLParameters(URI)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(
        queue=str(QUEUE_PRODUCER),
        durable=True,
        arguments={"x-queue-type": "classic"}
    )
    print(f"Quees creada: {QUEUE_PRODUCER}")
    time.sleep(3)
    channel.exchange_declare(exchange=EXCHANGE_QUEUE, durable=True)
    channel.queue_bind(exchange=EXCHANGE_QUEUE,
                       queue=QUEUE_PRODUCER, routing_key=ROUTING_KEY)
    print("ROUNTING_KEY asociado")

except Exception as error:
    print(f"Error en el proceso: {str(error)}")