from django.db import models

from ambassadors.constants import (AMBASSADOR_STATUS_CHOICES,
                                   DECIMAL_MAX_DIGITS, DECIMAL_PLACES,
                                   GOAL_MAX_LEN, GUIDE_STATUS_CHOICES,
                                   NAME_MAX_LEN, SIZE_MAX_LEN, STATUS_MAX_LEN)
from ambassadors.validators import POSTAL_CODE_VALIDATOR


class Ambassador(models.Model):
    pass


class Action(models.Model):
    action = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Действие"
    )

    class Meta:
        verbose_name = "Действие в рамках амбассадоров"
        verbose_name_plural = "Действия в рамках амбассадоров"
        ordering = ['name']

    def __str__(self):
        return self.action


class AmbassadorAction(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        related_name="ambassador_actions",
        verbose_name="ID амбассадора"
    )
    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE,
        related_name="ambassador_actions",
        verbose_name="ID действия"
    )

    class Meta:
        verbose_name = "Амбассадор-Действие"
        verbose_name_plural = "Амбассадор-Действия"

    def __str__(self):
        return f"{self.ambassador} - {self.action}"


class Goal(models.Model):
    goal = models.CharField(
        max_length=GOAL_MAX_LEN,
        verbose_name="Цель в практикуме"
    )

    class Meta:
        verbose_name = "Цель в Практикуме"
        verbose_name_plural = "Цели в Практикуме"

    def __str__(self):
        return self.goal


class Address(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name="Амбассадор"
    )
    country = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Страна",
    )
    city = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Город",
    )
    postal_code = models.PositiveIntegerField(
        verbose_name="Почтовый индекс",
        validators=(POSTAL_CODE_VALIDATOR,)
    )
    street = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Улица",
    )
    house_number = models.PositiveSmallIntegerField(
        verbose_name="Дом"
    )
    apartment_number = models.PositiveSmallIntegerField(
        verbose_name="Квартира"
    )

    class Meta:
        verbose_name = "Адрес амбассадора"
        verbose_name_plural = "Адреса амбассадора"

    def __str__(self):
        return (
            f"{self.country}, "
            f"{self.city}, "
            f"{self.street} "
            f"{self.house_number}, "
            f"кв. {self.apartment_number}"
            )


class ClothingSize(models.Model):
    size = models.CharField(
        max_length=SIZE_MAX_LEN,
        verbose_name="Размер одежды"
    )

    class Meta:
        verbose_name = "Размер одежды"
        verbose_name_plural = "Размер одежды"

    def __str__(self):
        return self.size


class FootSize(models.Model):
    size = models.PositiveSmallIntegerField(
        verbose_name="Размер ноги"
    )

    class Meta:
        verbose_name = "Размер ноги"
        verbose_name_plural = "Размер ноги"

    def __str__(self):
        return self.size


class Course(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Направление обучения в Практикуме"
    )

    class Meta:
        verbose_name = "Направление обучения в Практикуме"
        verbose_name_plural = "Направления обучения в Практикуме"
        ordering = ['name']

    def __str__(self):
        return self.name


class AmbassadorStatus(models.Model):
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=AMBASSADOR_STATUS_CHOICES,
        verbose_name="Статус амбассадора"
    )

    class Meta:
        verbose_name = "Статус амбассадора"
        verbose_name_plural = "Статус амбассадора"

    def __str__(self):
        return self.get_status_display()


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
