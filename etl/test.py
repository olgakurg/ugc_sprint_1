# from kafka import KafkaConsumer
# from kafka import KafkaProducer
# from time import sleep


# producer = KafkaProducer(bootstrap_servers=['localhost:29392'])

# producer.send(
#     topic='messages',
#     value=b'my message from python',
#     key=b'python-message',
# )

# sleep(1)


# consumer = KafkaConsumer(
#     'messages',
#     bootstrap_servers=['localhost:29392'],
#     auto_offset_reset='earliest',
#     group_id='echo-messages-to-stdout',
# )

# for message in consumer:
#     print(message.value)


# from clickhouse_driver import Client

# client = Client(host='localhost')


# res = client.execute('SELECT * FROM default.movies_progress')

# print(res)


# if __name__ == '__main__':
#     kafka = KafkaMesseger(f'{settings.bus_address}:{settings.bus_port}')

#     asyncio.run(start(kafka))async
# from aiohttp import ClientSession
# from aiochclient import ChClient
# import asyncio
# import json
# from aiokafka import AIOKafkaConsumer
# from sourcemes import SouceMessager


# class KafkaMesseger(SouceMessager):
#     def __init__(self, brocker):
#         self.brocker = brocker

#     async def read(self, source):
#         consumer = AIOKafkaConsumer(
#             source,
#             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
#             bootstrap_servers='localhost:29392',
#         )
#         await consumer.start()

#         async for msg in consumer:
#             print(msg.value)
#             print(type(msg.value))


# async def start(bus):

#     await asyncio.gather(bus.read('messages'), bus.read('tutut'))


# if __name__ == '__main__':
#     kafka = KafkaMesseger("")

#     asyncio.run(start(kafka))


# async def main():
#     async with ClientSession() as s:
#         client = ChClient(s)
#         assert await client.is_alive()

import asyncio
from aiochclient import ChClient
from aiohttp import ClientSession


async def main():
    async with ClientSession() as s:
        client = ChClient(s, url="http://localhost:8123")
        test = await client.is_alive()
        print(test)


if __name__ == '__main__':
    asyncio.run(main())
