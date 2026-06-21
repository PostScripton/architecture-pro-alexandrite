# Задание 2. Мониторинг

Сайт «Александрит» подключён к Яндекс Метрике. Но с тех пор, как бизнес начал предоставлять оформление заказов через API, данные Яндекс Метрики уже не дают полной картины. Чтобы начать улучшать систему, вам нужно от чего-то отталкиваться. В этом задании вы запланируете внедрение мониторинга.

Вам нужно определить, что вы хотите измерять и как вы будете это делать. А затем — постараться обосновать свои решения для бизнеса. Не забывайте: бизнесу не всегда очевидно, что мониторинг стоит того, чтобы выделять на него ресурсы команды.

### Что нужно сделать

1. **Создайте в директории Task2 текстовый файл и назовите его «Выбор и настройка мониторинга в системе».** Вы будете оформлять своё решение в виде технического документа.
2. **Проанализируйте систему компании и C4-диаграмму в контексте планирования мониторинга.**
3. **Добавьте в файл раздел «Мотивация».** Напишите здесь, почему в систему нужно добавить мониторинг и что это даст компании.
4. **Добавьте раздел «Выбор подхода к мониторингу».** Выберите, какой подход к мониторингу вы будете использовать: RED, USE или «Четыре золотых сигнала». Для разных частей системы можно использовать разные подходы.
5. **Опишите, какие метрики и в каких частях системы вы будете отслеживать.** Перед вами список метрик. Выберите метрики, которые вы считаете нужным отслеживать. Для выбранных метрик напишите:
   - Зачем нужна эта метрика.
   - Нужны ли ярлыки для этой метрики. Если ярлыки нужны, опишите, какие именно вы планируете добавить.
     Вы можете не ограничивать себя только этим списком. Если вы видите, что стоит добавить какие-то ещё метрики, — добавьте и их тоже.

<details>
<summary>Список возможных метрик для отслеживания</summary>

1. Number of `dead-letter-exchange` letters in RabbitMQ
2. Number of message `in flight` in RabbitMQ
3. Number of requests (RPS) for internet shop API
4. Number of requests (RPS) for CRM API
5. Number of requests (RPS) for MES API
6. Number of requests (RPS) per user for internet shop API
7. Number of requests (RPS) per user for CRM API
8. Number of requests (RPS) per user for MES API
9. CPU % for shop API
10. CPU % for CRM API
11. CPU % for MES API
12. Memory Utilisation for shop API
13. Memory Utilisation for CRM API
14. Memory Utilisation for MES API
15. Memory Utilisation for shop db instance
16. Memory Utilisation for MES db instance
17. Number of connections for shop db instance
18. Number of connections for MES db instance
19. Response time (latency) for shop API
20. Response time (latency) for CRM API
21. Response time (latency) for MES API
22. Size of S3 storage
23. Size of shop db instance
24. Size of MES db instance
25. Number of `HTTP 200` for shop API
26. Number of `HTTP 200` for CRM API
27. Number of `HTTP 200` for MES API
28. Number of `HTTP 500` for shop API
29. Number of `HTTP 500` for CRM API
30. Number of `HTTP 500` for MES API
31. Number of `HTTP 500` for shop API
32. Number of simultanious sessions for shop API
33. Number of simultanious sessions for CRM API
34. Number of simultanious sessions for MES API
35. Kb tranferred (received) for shop API
36. Kb tranferred (received) for CRM API
37. Kb tranferred (received) for MES API
38. Kb provided (sent) for shop API
39. Kb provided (sent) for CRM API
40. Kb provided (sent) for MES API

</details>

6. **Добавьте раздел «План действий».** Напишите высокоуровнево, какие задачи вы видите для реализации. Это будет драфт технического задания. Например, «Создать инстанс time-series базы с использованием такой-то технологии».
7. **Дополнительное задание.** Выберите показатели насыщенности — определите, что является пороговым значением насыщенности и почему нужно использовать именно такие показатели. Опишите, что должно происходить в системе в случае, если эти параметры будут превышены. Например, нужно завести тикет, добавить инстансов, написать письмо в саппорт, добавить автоматическую «звонилку» и так далее. Если вы сдадите работу без этого пункта, это не повлияет на проверку задания ревьюером.
