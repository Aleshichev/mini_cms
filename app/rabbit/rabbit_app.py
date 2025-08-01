# import pika
# import logging

# RMQ_HOST = "localhost"
# RMQ_PORT = 5672
# RMQ_USER = "guest"
# RMQ_PASS = "guest"

# MQ_EXCHANGE = ""
# MQ_ROUTING_KEY = "news"

# connection_params = pika.ConnectionParameters(
#     host=RMQ_HOST,
#     port=RMQ_PORT,
#     credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASS),
# )


# def get_connection() -> pika.BlockingConnection:
#     return pika.BlockingConnection(
#         parameters=connection_params,
#     )


# def configure_logging(level: int = logging.INFO):
#     logging.basicConfig(
#         level=level,
#         datefmt="%Y-%m-%d %H:%M:%S",
#         format="[%(asctime)s.%(msecs)03d] %(funcName)20s %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
#     )
