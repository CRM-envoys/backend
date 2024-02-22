# backend CRM
![python version](https://img.shields.io/badge/Python-3.11-green)
![django version](https://img.shields.io/badge/Django-4.2-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.14-green)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
### Оглавление:
- [Бэкенд CRM для Амбассадоров Яндекс Практикума](#бэкенд-CRM)
    - [О проекте:](#о-проекте)
    - [Оглавление:](#оглавление)
  - [Запуск приложения](#запуск-приложения)
      - [Запуск приложения на локальном сервере](#запуск-приложения-на-локальном-сервере)
      - [Запуск тестов:](#запуск-тестов)
      - [Документация API доступна по адресам:](#документация-api-доступна-по-адресам)
      - [Админка доступна по адресу:](#админка-доступна-по-адресу)
    - [Установка pre-commit hooks](#установка-pre-commit-hooks)
      - [Установка pre-commit](#установка-pre-commit)
      - [Установка hooks](#установка-hooks)
    - [Работа с commitizen](#работа-с-commitizen)
  - [Используемые технологии](#используемые-технологии)
  - [Авторы](#авторы)

### О проекте:
CRM-система для Амбассадоров Яндекс Практикума - это пространство для комьюнити менеджера сообщества амбассадоров, в котором можно получать уведомления, делать рассылки и смотреть аналитику. 

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
- [Смирнов Артем](https://github.com/BeardedDev1911)
