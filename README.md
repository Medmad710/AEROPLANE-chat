# WebSocket Real-Time Chat (WhatsApp Style)

[cite_start]Данный проект представляет собой чат в реальном времени, разработанный в рамках курса «WebSockets Protocol Explained».

## Особенности
* [cite_start]**Real-time Messaging:** Мгновенная передача сообщений без задержек и перезагрузок страницы[cite: 206].
* **User Persistence:** Ваш никнейм сохраняется в браузере (localStorage).
* **Chat History:** Вся переписка сохраняется в `messages.json` на сервере и доступна после перезапуска.
* **WhatsApp UI:** Визуальное разделение своих и чужих сообщений, характерная цветовая схема.

## [cite_start]Структура проекта [cite: 238, 243]
* `server.py` — Серверная часть на Python (библиотека websockets).
* `index.html` — Клиентская часть (HTML/CSS/JS).
* `messages.json` — Файл базы данных для хранения истории (создается автоматически).

## [cite_start]Инструкция по запуску [cite: 191]

### 1. Установка зависимостей
Для работы сервера необходима библиотека `websockets`. Установите её через pip:
```bash
pip install websockets
