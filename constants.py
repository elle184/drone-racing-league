import os
from dotenv import load_dotenv

load_dotenv()

URI = f"{os.environ.get('URI')}?heartbeat=600&retry_delay=10&blocked_connection_timeout=600"
QUEUE_CONSUMER = os.getenv("CONSUME_QUEUE")
QUEUE_PRODUCER = os.getenv("PRODUCER_QUEUE")
SSL_CONNECTION = int(os.environ.get("SSL_CONNECTION", 0))
PREFETCH_COUNT = int(os.environ.get("PREFETCH_COUNT", 1))
CIPHER_KEY = os.environ.get("CIPHER_KEY")
EXCHANGE_QUEUE = os.getenv("EXCHANGE_QUEUE")
ROUTING_KEY = os.getenv("ROUTING_KEY")

MAX_CONSUMER_RETRIES = int(
    os.environ.get("MAX_CONSUMER_RETRIES", 2)
)
RETRY_DELEY_CONSUMER = int(
    os.environ.get("RETRY_DELEY_CONSUMER", 5)
)   # Segundos
MAX_CONNECTION_RETRIES = int(
    os.environ.get("MAX_CONNECTION_RETRIES", 2)
)
RETRY_DELAY_CONNECTION = int(
    os.environ.get("RETRY_DELAY_CONNECTION", 1)
)   # Segundos
MAX_PUBLISH_RETRIES = int(
    os.environ.get("MAX_PUBLISH_RETRIES", 2)
)
RETRY_DELAY_PUBLISH = int(
    os.environ.get("RETRY_DELAY_PUBLISH", 1)
)   # Segundos

POSTGRESQL_DB = os.getenv("POSTGRESQL_DB")
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_PORT = os.getenv("POSTGRESQL_PORT")

RUN_SERVER = os.getenv("RUN_SERVER")
RUN_WORKER = os.getenv("RUN_WORKER")