import logging

from confluent_kafka.admin import AdminClient, NewTopic
from core.config import Settings
from models import MovieProgress, MovieRes, ClickElement, FilterQuery, PageDuration

kafka_topics = {
    MovieProgress: "some_topic",
    MovieRes: "some_topic",
    ClickElement: "some_topic",
    FilterQuery: "some_topic",
    PageDuration: "some_topic",
}


def create_topics(settings: Settings):
    topics = kafka_topics.values()
    logging.info(f'trying to create topics {topics}')
    a = AdminClient({'bootstrap.servers': '{}:{}'.format(settings.kafka_host, settings.kafka_port)})
    new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in topics]
    fs = a.create_topics(new_topics)
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            logging.info("Topic {} created".format(topic))
        except Exception as e:
            logging.info("Failed to create topic {}: {}".format(topic, e))
