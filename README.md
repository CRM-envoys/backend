# backend CRM
![example workflow](https://github.com/CRM-for-Yandex-ambassadors/backend/actions/workflows/workflow.yaml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![python version](https://img.shields.io/badge/Python-3.11-green)
![django version](https://img.shields.io/badge/Django-4.2-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.14-green)


### [Сайт учета Амбасадоров](http://devinse.store/admin/)

## Оглавление:
- [backend CRM](#backend-crm)
    - [О проекте](#о-проекте)
  - [Запуск приложения](#запуск-приложения)
      - [Запуск приложения на локальном сервере](#запуск-приложения-на-локальном-сервере)
      - [Запуск тестов](#запуск-тестов)
    - [Установка pre-commit hooks](#установка-pre-commit-hooks)
      - [Установка pre-commit](#установка-pre-commit)
      - [Установка hooks](#установка-hooks)
      - [Работа с commitizen](#работа-с-commitizen)
  - [Используемые технологии](#используемые-технологии)
  - [Авторы](#авторы)
  - [Swagger](#Swagger)

## О проекте:
CRM-система для Амбассадоров Яндекс Практикума - это пространство для комьюнити менеджера сообщества амбассадоров, в котором можно получать уведомления, делать рассылки и смотреть аналитику. 

## Запуск приложения
**Клонирование реппозитория**

```sh
git clone git@github.com:CRM-for-Yandex-ambassadors/backend.git
```

Перейдите в папку с проектом backend, установите и запустите виртуальное окружение.

```sh
cd recruitment-process-back
```

```sh
python -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```
**Установка зависимостей**

  ```sh
  pip install -r requirements.txt
  ```
**Применяем миграции:**

  ```sh
  python manage.py migrate
  ```
**Создаем суперпользователя:**

  ```
  python manage.py createsuperuser
  ```

#### Запуск приложения на локальном сервере
Перейдите в папку crm_backend
```sh
cd crm_backend
```

* Если у вас windows
    ```sh
    python manage.py runserver
    ```
* Если у вас Linux/MacOS
    ```sh
    python3 manage.py runserver
    ```

#### Запуск тестов
```sh
python manage.py test
```
Для проверки процента покрытия тестами вам необходимо установить библиотеку coverage и выполнить команды:
```sh
pip install coverage
```
```sh
coverage run -m unittest discover
```
```sh
coverage report -m
```

### Установка pre-commit hooks

Для того, чтобы при каждом коммите выполнялись pre-commit проверки, необходимо:
- Установить pre-commit
- Установить pre-commit hooks

#### Установка pre-commit
Модуль pre-commit уже добавлен в requirements и должен установиться автоматически с виртуальным окружением.

Проверить установлен ли pre-commit можно командой (при активированном виртуальном окружении):
```sh
pre-commit --version
>> pre-commit 3.3.3
```

Если этого не произошло, то необходимо установить pre-commit:
```sh
pip install pre-commit
```

#### Установка hooks
Установка хуков:
```sh
pre-commit install --all
```
Установка хука для commitizen
```sh
pre-commit install --hook-type commit-msg
```
В дальнейшем, при выполнении команды git commit будут выполняться проверки, перечисленные в файле .pre-commit-config.yaml.

Если не видно, какая именно ошибка мешает выполнить commit, можно запустить хуки вручную командой:
```sh
pre-commit run --all-files
```

#### Работа с commitizen
Чтобы сгенерировать установленный git-commit, запустите в вашем терминале
```sh
cz commit
```
или сочетание клавиш
```sh
cz c
```

## Используемые технологии
- Python 3.11
- Django 4.2
- Django Rest Framework 3.14.0

## Авторы
- [Балахонова Марина](https://github.com/margoloko)
- [Виноградов Сергей](https://github.com/yan-gabala)
- [Раскатов Андрей](https://github.com/Diavolution)
- [Климов Артем](https://github.com/grinchomsk)

## Swagger
[Swagger](https://drive.google.com/file/d/1Kbyb8UvEl_VYOHmAaI1J2HfvSLDgcuGT/view?usp=drive_link)
