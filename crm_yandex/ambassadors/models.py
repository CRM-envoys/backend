from core.constants import Limits
from django.db import models

from ambassadors.validators import (POSTAL_CODE_VALIDATOR,
                                    PHONE_NUMBER_VALIDATOR,
                                    TELEGRAM_USERNAME_VALIDATOR)




class Ambassador(models.Model):
    """
    Модель повторяет ЯФ + заметки КМ руками.
    еще не все поля прописаны
    """
    fio = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name='ФИО'
    )
    gender = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name='Пол'
    )
    course = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name='Курс'
    )
    country = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Страна",
    )
    city = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Город",
    )
    adress = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Адрес",
    )
    postal_code = models.PositiveIntegerField(
        verbose_name="Почтовый индекс",
        validators=(POSTAL_CODE_VALIDATOR,)
    )
    email = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Электронная почта",
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона",
        validators=(TELEGRAM_USERNAME_VALIDATOR,)
    )
    nickname_telegram = models.CharField(
        verbose_name="Ник в телеграм",
        validators=(PHONE_NUMBER_VALIDATOR,)
    )
    education = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Образование",
    )
    place_work = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Место работы",
    )
    goal = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Цель обучения",
    )
    want_do_as_ambassador = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Напраление работы амбассадора",
    )
    blog_ambassador = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Блог амбассадора",
    )
    size = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Размер одежды",
    )
    foot_size = models.CharField(
        max_length=Limits.NAME_MAX_LEN.value,
        verbose_name="Размер обуви",
    )
    about_me = models.CharField(  ### последнее поле из ЯФ ###
        verbose_name="О себе",
    )
    status = models.CharField(  ### далее поля задает КМ ###
        choices=Limits.AMBASSADOR_STATUS_CHOICES.value,
        verbose_name="Статус амбассадора"
    )
    # status_profile = models.BooleanField


    class Meta:
        verbose_name = "Амбассадор"
        verbose_name_plural = "Амбассадоры"
        ordering = ['-date'] # сортировка держит сверху самую свежую анкету из ЯФ






"""

class Action(models.Model):  # Вариант для интеграции ЯФ (Нам приходит готовая строка)
    action = models.CharField(  # Если нет, то через CHOICE вбивает КМ:
        max_length=Limits.NAME_MAX_LEN.value,  # Вести блог, Писать статьи (полный перечень в ЯФ)
        verbose_name="Действие"
    )
    slug = models.SlugField(
        verbose_name='Ссылка на курс',
        max_length=Limits.DESIGNATION.value,
        null=True,
        unique=True
    )

    class Meta:
        verbose_name = "Действие в рамках амбассадоров"
        verbose_name_plural = "Действия в рамках амбассадоров"
        ordering = ['name']

    def __str__(self):
        return self.action


class Goal(models.Model):  # Вариант для интеграции ЯФ (Нам приходит готовая строка)
    goal = models.CharField(  # Если нет, то через CHOICES вбивает КМ:
        max_length=Limits.GOAL_MAX_LEN.value, # Получение новой профессии (полный перечень в ЯФ)
        verbose_name="Цель в практикуме"
    )

    class Meta:
        verbose_name = "Цель в Практикуме"
        verbose_name_plural = "Цели в Практикуме"

    def __str__(self):
        return self.goal


class Ambassador_old(models.Model): # Если интег-ция с ЯФ, то все поля из ЯФ в модели - CharField
    action = models.ManyToManyField( # моделью м.б. только, то что подвязыает руками КM
        Action,  # вполне достаточно CHOICES
        related_name='ambassadors', # Резюмирую: модели action, goal излишни в проекте
        verbose_name="Действия в рамках амбассадоров" 
    )
    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        related_name='ambassadors',
        verbose_name="Цель в практикуме"
    )



















class AmbassadorProfileStatus(models.Model):
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        verbose_name="Статус профиля амбассадора"
    )

    class Meta:
        verbose_name = "Статус профиля амбассадора"
        verbose_name_plural = "Статус профиля амбассадора"

    def __str__(self):
        return self.status


class Merch(models.Model):
    merch_type = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Мерч"
    )
    cost = models.DecimalField(
        max_digits=DECIMAL_MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        verbose_name="Стоимость"
    )

    class Meta:
        verbose_name = "Мерч"
        verbose_name_plural = "Мерчи"
        ordering = ['merch_type']

    def __str__(self):
        return f"{self.merch_type} - {self.cost}"


class MerchShipment(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        related_name="merch_shipments",
        verbose_name="ID амбассадора"
    )
    date = models.DateField()

    class Meta:
        verbose_name = "Отправка мерча"
        verbose_name_plural = "Отправки мерча"
        ordering = ['-date']


class MerchOnShipping(models.Model):
    shipping = models.ForeignKey(
        MerchShipment,
        on_delete=models.CASCADE,
        related_name="merch_on_shipping",
        verbose_name="ID отправки"
    )
    merch = models.ForeignKey(
        Merch,
        on_delete=models.CASCADE,
        related_name="merch_on_shipping",
        verbose_name="Мерч"
    )
    size = models.CharField(
        max_length=SIZE_MAX_LEN,
        verbose_name="Размер"
    )

    class Meta:
        verbose_name = "Мерч в отправке"
        verbose_name_plural = "Мерч в отправке"

    def __str__(self):
        return f"{self.merch} - {self.size}"


class Venue(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Название площадки"
    )

    class Meta:
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"
        ordering = ['name']

    def __str__(self):
        return self.name


class Content(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        related_name="content",
        verbose_name="Амбассадор"
    )
    link = models.URLField()
    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        related_name="content",
        verbose_name="Площадка"
    )
    date = models.DateField()
    guide_followed = models.BooleanField(verbose_name="По гайду да/нет")

    class Meta:
        verbose_name = "Контент амбассадора"
        verbose_name_plural = "Контент амбассадора"
        ordering = ['-date']

    def __str__(self):
        return (
            f"Амбассадор: {self.ambassador} {self.link}"
        )


class OnboardingStatus(models.Model):
    status = models.BooleanField(
        verbose_name="Статус выполнения онбординга"
    )

    class Meta:
        verbose_name = "Статус выполнения онбординга"
        verbose_name_plural = "Статус выполнения онбординга"

    def __str__(self):
        return self.status


class GuideStatus(models.Model):
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=GUIDE_STATUS_CHOICES,
        verbose_name="Статус выполнения гайда"
    )

    class Meta:
        verbose_name = "Статус выполнения гайда"
        verbose_name_plural = "Статус выполнения гайда"

    def __str__(self):
        return self.get_status_display()
"""