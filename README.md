# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.

## Требования

Для работы приложения у вас должен быть установлен python версии 3.8 и выше.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/dad-siberian/dvmn_django_1.git
    ```

2. Перейдите в каталог проекта:

    ```bash
    cd dvmn_django_1
    ```

3. Создайте виртуальное окружение:

    ```bash
    python -m venv .venv
    ```

4. Активируйте виртуальное окружение:

    - Для Windows:

    ```bash
    .venv\Scripts\activate
    ```

    - Для macOS и Linux:

    ```bash
    source .venv/bin/activate
    ```

5. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

6. Примените миграции:

    ```bash
    python manage.py migrate
    ```

7. Создайте суперпользователя

    ```bash
    python manage.py createsuperuser
    ```

## Запуск

Выполните следующую команду для запуска Django:

```bash
python manage.py runserver
