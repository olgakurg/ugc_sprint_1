
from core.config import Settings
from kafka3.admin import KafkaAdminClient, NewTopic
from models import MovieProgress, MovieRes, ClickElement, FilterQuery, PageDuration

kafka_topics = {
    MovieProgress: "movies_progress",
    MovieRes: "movie_resolution",
    ClickElement: "click_element",
    FilterQuery: "filter_query",
    PageDuration: "page_duration",

}


def create_topic(topic_name, settings: Settings):
    admin_client = KafkaAdminClient(bootstrap_servers=f'{settings.kafka_host}:{settings.kafka_host}')
    topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)
    admin_client.create_topics(new_topics=[topic], validate_only=False)


def create_all_topics(kafka_topics, settings: Settings):
    for topic_name in kafka_topics.values():
        create_topic(topic_name, settings)
