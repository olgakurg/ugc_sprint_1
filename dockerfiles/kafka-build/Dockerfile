FROM openjdk:11.0.16-jre-slim-buster


RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*


ENV KAFKA_VERSION 3.6.1
ENV SCALA_VERSION 2.13


RUN mkdir -p /tmp-download/kafka && \
    curl -L "https://archive.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" \
    -o /tmp-download/kafka/kafka.tgz && \
    mkdir /kafka && tar -xvzf /tmp-download/kafka/kafka.tgz -C /kafka --strip 1 && \
    rm -rf /tmp-download


RUN mkdir -p /kafka-data/kraft-combined-logs


COPY start.sh /usr/bin/
RUN chmod +x usr/bin/start.sh


CMD ["usr/bin/start.sh"]