import logging

from confluent_kafka.admin import AdminClient, NewTopic
from core.config import Settings

# A dictionary to hold Kafka topics
KAFKA_TOPICS = {
    "MovieProgress": "some_topic",
    "MovieRes": "some_topic",
    "ClickElement": "some_topic",
    "FilterQuery": "some_topic",
    "PageDuration": "some_topic",
}


def create_topics(settings: Settings) -> None:
    """
    Function to create Kafka topics.

    Args:
        settings (Settings): The settings for the Kafka instance.

    Returns:
        None
    """
    topics = KAFKA_TOPICS.values()
    logging.info(f'Trying to create topics {topics}')
    try:
        admin_client = AdminClient({
            'bootstrap.servers': f'{settings.kafka_host}:{settings.kafka_port}'
        })
        new_topics = [
            NewTopic(topic, num_partitions=3, replication_factor=1)
            for topic in topics
        ]
        fs = admin_client.create_topics(new_topics)
    except Exception as e:
        logging.info(f"Failed to connect with Kafka instance with {e}")
        return

    for topic, f in fs.items():
        try:
            f.result()
            logging.info(f"Topic {topic} created")
        except Exception as e:
            logging.info(f"Failed to create topic {topic}: {e}")
