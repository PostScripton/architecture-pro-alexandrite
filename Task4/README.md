# Задание 4. Логирование

Технический документ: `Архитектурное решение по логированию.md`

## Архитектурное решение (задание 4)

**Системы под логированием:** Shop API, CRM API, MES API, RabbitMQ.

**Стек:** Fluent Bit (сбор) -> Logstash (обработка и маскирование PII) -> OpenSearch Managed в Yandex Cloud (хранение) -> OpenSearch Dashboards (визуализация и алертинг).

Сервисы пишут структурированные JSON-логи в stdout. Fluent Bit собирает их с каждого EC2-инстанса, добавляет метаданные (окружение, версия сервиса). Logstash маскирует чувствительные поля и маршрутизирует по раздельным индексам на сервис.

**Ключевые события с уровнем INFO:** переходы статусов заказа (`order_id`, `status_from`, `status_to`), публикация и получение сообщений RabbitMQ (`order_id`, `message_id`, `queue_name`), расчёт стоимости в MES API (`order_id`, `duration_ms`, `calculated_price`), HTTP-запросы (`method`, `path`, `http_status`, `duration_ms`).

**Приоритет внедрения:** сначала CRM API + MES API + RabbitMQ (где теряются заказы), затем Shop API, фронтенды - в последнюю очередь.

**Политика безопасности:** персональные данные клиентов в логах запрещены, только технические идентификаторы. Доступ через VPN + SSO с ролевой моделью (developer / devops / support).

**Политика хранения:** ERROR - 90 дней, INFO - 30 дней, DEBUG - 7 дней (только dev/release). Раздельные индексы по сервису и окружению с ILM.

**Алертинг:** заказ завис в SUBMITTED > 5 минут, заказ завис в PRICE_CALCULATED > 35 минут, сообщение в dead-letter очереди, > 10 ошибок за 5 минут в любом сервисе, отсутствие логов от сервиса > 2 минут.

**Технология:** OpenSearch (Apache 2.0, Managed в Yandex Cloud) выбран вместо ELK (лицензионные риски SSPL), Splunk (запретительная цена) и Loki (ограниченный полнотекстовый поиск).

Диаграмма с компонентами логирования (оранжевым):

<img src="/images/tasks/Task4/jewerly_c4_model_logging.svg" alt="C4 Container Diagram with Logging Infrastructure"/>
