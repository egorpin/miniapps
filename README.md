![image](https://github.com/user-attachments/assets/281ebaae-5bb2-4939-900c-470e1fb8cdb2)

# Интернет-магазин в Telegram Mini Apps

Этот проект представляет собой пример интернет-магазина, реализованного с использованием Telegram Mini Apps. Он состоит из клиентской части (веб-приложение, размещенное по внешней ссылке) и серверной части (на Python с использованием Flask), а также Telegram-бота на базе библиотеки aiogram для интеграции с Telegram.

## Предварительные требования

* **Python 3.7+**
* **Установленные библиотеки:**
    ```bash
    pip install aiogram python-dotenv Flask Flask-CORS
    ```
* **Telegram Bot Token:** Получите токен нового бота у [BotFather](https://t.me/BotFather) в Telegram.
* **Внешний хостинг:** Для размещения статических файлов Mini App (`index.html`, `css`, `js` и т.д.) вам потребуется внешний веб-хостинг (например, GitHub Pages, Vercel, Netlify).
* **(Опционально) Сервер для API:** Если вы планируете использовать серверную часть (`api.py`) для хранения данных, обработки заказов и т.д., вам потребуется сервер для его запуска (локально для разработки или удаленный сервер для продакшена).

## Настройка

1.  **Клонируйте репозиторий (если используете Git):**
    ```bash
    git clone [https://github.com/new](https://github.com/new)
    cd your_project
    ```

2.  **Создайте файл `.env`:**
    В корневой директории проекта создайте файл `.env` и добавьте туда токен вашего Telegram-бота:
    ```
    BOT_TOKEN=YOUR_BOT_TOKEN
    ```
    Замените `YOUR_BOT_TOKEN` на фактический токен вашего бота.

3.  **Настройте URL Mini App в `bot.py`:**
    Откройте файл `bot.py` и замените `ВАША_ССЫЛКА_НА_МИНИ_ПРИЛОЖЕНИЕ` на URL, по которому размещена главная страница вашего Mini App (`index.html`).
    ```python
    web_app_info = types.WebAppInfo(url="[https://your-hosting.com/your-mini-app/](https://your-hosting.com/your-mini-app/)")
    ```

4.  **(Опционально) Запустите серверную часть (`api.py`):**
    Если вы планируете использовать API, запустите сервер Flask:
    ```bash
    python api.py
    ```
    Сервер будет запущен по адресу `http://127.0.0.1:5000/` (по умолчанию).

5.  **Разместите статические файлы Mini App:**
    Загрузите содержимое директории `static` на ваш веб-хостинг. Убедитесь, что файл `index.html` доступен по URL, указанному в `bot.py`.

## Запуск

1.  **Запустите Telegram-бота:**
    ```bash
    python bot.py
    ```
    Бот начнет принимать команды в Telegram.

2.  **Используйте команду `/start` в Telegram:**
    Откройте Telegram и найдите своего бота. Отправьте ему команду `/start`. Бот должен отправить сообщение с кнопкой "Открыть магазин", которая откроет ваше Mini App.

## Функциональность

* **`/start` команда:** Открывает Mini App с интернет-магазином.
* **Отображение товаров (Mini App):** Клиентская часть Mini App должна отображать каталог товаров, получая данные (в данном примере) непосредственно в коде или через API (`/api/products`).
* **Добавление в корзину (Mini App):** Пользователи могут добавлять товары в корзину.
* **Отправка данных из Mini App боту:** При закрытии Mini App (например, после оформления заказа), данные могут быть отправлены боту, который обрабатывает их в функции `web_app_data` (`bot.py`).
* **API (серверная часть):**
    * `/api/products` (GET): Возвращает список товаров.
    * `/api/products/<product_id>` (GET): Возвращает информацию о конкретном товаре.
    * `/api/cart/add` (POST): Пример обработки добавления товара в корзину (логирование на сервере).
    * `/api/orders/create` (POST): Пример обработки оформления заказа (логирование на сервере).
    * `/` (GET): Отображает главную страницу Mini App (`index.html`).
