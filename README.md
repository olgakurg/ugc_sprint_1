# Проектная работа 8 спринта


###Инструкции по запуску проекта.

# Проектная работа 8 спринта

### Инструкции по запуску проекта.

1. Для запуска необходимы файлы env, заполненные по образцам:

* src/.env для запуска API:
  `
  project_name=movies_transport
  kafka_host=kafka_1
  kafka_port=9092 `

* #etl/.env.etl для запуска etl:
  `
  db_address=0.0.0.0
  db_port=8123
  event_table=events
  bus_address=0.0.0.0
  bus_port=29392
  topics_str=movies_progress
  batch_size=100
  topics=[movies_progress]`

2. Для развертывания кластеров ClickHouse и Kafka, API и УЕД необходимо выполнить в консоли команду:
   '''docker-compose up --build -d'''




