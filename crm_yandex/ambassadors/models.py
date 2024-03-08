from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q

from .constants import (AMBASSADOR_STATUS_CHOICES, CLOTHING_SIZE_CHOICES,
                        CLOTHING_SIZE_MAX_LEN, COURSE_CHOICES,
                        DECIMAL_MAX_DIGITS, DECIMAL_PLACES, GOAL_MAX_LEN,
                        NAME_MAX_LEN, PHONE_NUM_MAX_LEN,
                        PROMOCODE_MAX_LEN, SEX_CHOICES, SEX_MAX_LEN,
                        SHIPMENT_STATUS_CHOICES, STATUS_MAX_LEN,
                        TELEGRAM_MAX_LEN)

from .validators import POSTAL_CODE_VALIDATOR, TELEGRAM_USERNAME_VALIDATOR


class Activity(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Действие"
    )

    class Meta:
        verbose_name = "Действие в рамках амбассадорства"
        verbose_name_plural = "Действия в рамках амбассадорства"
        ordering = ["name"]

    def __str__(self):
        return self.name


class AmbassadorManager(models.Manager):
    def get_queryset(self):
        ambassadors = super().get_queryset()

        new_ambassadors = ambassadors.filter(viewed=False)
        new_content = ambassadors.filter(
            content__guide_followed=True,
            content__viewed=False
        )
        other_ambassadors = ambassadors.exclude(Q(viewed=False) | Q(
                content__guide_followed=True, content__viewed=False)
                ).order_by("-registration_date")
        queryset = new_ambassadors | new_content | other_ambassadors

        return queryset


class Ambassador(models.Model):
    fio = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Фамилия Имя Отчество"
    )
    sex = models.CharField(
        max_length=SEX_MAX_LEN,
        choices=SEX_CHOICES,
        verbose_name="Пол амбассадора"
    )
    course = models.CharField(
        max_length=NAME_MAX_LEN,
        choices=COURSE_CHOICES,
        verbose_name="Программа обучения"
    )
    country = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Страна",
    )
    city = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Город",
    )
    address = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Адрес проживания"
    )
    postal_code = models.PositiveIntegerField(
        verbose_name="Почтовый индекс",
        validators=(POSTAL_CODE_VALIDATOR,)
    )
    email = models.EmailField(verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=PHONE_NUM_MAX_LEN,
        verbose_name="Номер телефона"
    )
    telegram = models.CharField(
        max_length=TELEGRAM_MAX_LEN,
        verbose_name="Телеграм",
        validators=(TELEGRAM_USERNAME_VALIDATOR,)
    )
    education = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Образование"
    )
    job = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Текущая работа"
    )
    goal = models.CharField(
        max_length=GOAL_MAX_LEN,
        verbose_name="Цель в Практикуме"
    )
    activities = models.ManyToManyField(
        Activity,
        through="AmbassadorActivity",
        verbose_name="Амбассадорские действия",
        related_name="ambassadors",
        through_fields=("ambassador", "activity")
    )
    blog_link = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка на блог"
    )
    clothing_size = models.CharField(
        max_length=CLOTHING_SIZE_MAX_LEN,
        choices=CLOTHING_SIZE_CHOICES,
        verbose_name="Размер одежды"
    )
    foot_size = models.PositiveSmallIntegerField(
        verbose_name="Размер ноги"
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий"
    )
    registration_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата регистрации",
        db_index=True
        )
    promocode = models.CharField(
        max_length=PROMOCODE_MAX_LEN,
        blank=True,
        null=True,
        verbose_name="Промокод"
    )
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=AMBASSADOR_STATUS_CHOICES,
        default="active",
        verbose_name="Статус амбассадора"
    )
    guide_one = models.BooleanField(
        default=False,
        verbose_name="Гайд 1"
    )
    guide_two = models.BooleanField(
        default=False,
        verbose_name="Гайд 2"
    )
    onboarding = models.BooleanField(
        default=False,
        verbose_name="Онбординг"
    )
    viewed = models.BooleanField(
        default=False,
        verbose_name="Просмотрено/не просмотрено"
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Обновлено"
    )
    objects = AmbassadorManager()

    class Meta:
        verbose_name = "Амбассадор"
        verbose_name_plural = "Амбассадоры"

    def __str__(self):
        return self.fio


class AmbassadorActivity(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        related_name="ambassador_activities",
        verbose_name="ID амбассадора"
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="ambassador_activities",
        verbose_name="ID действия"
    )

    class Meta:
        verbose_name = "Амбассадор-Действие"
        verbose_name_plural = "Амбассадор-Действия"

    def __str__(self):
        return f"{self.ambassador} - {self.activity}"


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
        ordering = ["merch_type"]

    def __str__(self):
        return f"{self.merch_type} - {self.cost}"


class MerchShipment(models.Model):
    curator = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Куратор"
    )
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        related_name="merch_shipments",
        verbose_name="ID амбассадора"
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата отправки",
        db_index=True
    )
    merches = models.ManyToManyField(
        Merch,
        through="MerchOnShipping",
        verbose_name="Амбассадорские действия",
        related_name="merch_shipments",
        through_fields=("shipping", "merch")
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий"
    )
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=SHIPMENT_STATUS_CHOICES,
        verbose_name="Статус отправки",
        default="unprocessed"
    )
    country = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Страна",
    )
    city = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Город",
    )
    address = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Адрес проживания"
    )
    postal_code = models.PositiveIntegerField(
        verbose_name="Почтовый индекс",
        validators=(POSTAL_CODE_VALIDATOR,)
    )
    phone_number = models.CharField(
        max_length=PHONE_NUM_MAX_LEN,
        verbose_name="Номер телефона"
    )

    class Meta:
        verbose_name = "Отправка мерча"
        verbose_name_plural = "Отправки мерча"
        ordering = ["-date"]

    def __str__(self):
        return f"Ambassador ID: {self.ambassador.id} - {self.date}"


class MerchOnShipping(models.Model):
    shipping = models.ForeignKey(
        MerchShipment,
        on_delete=models.CASCADE,
        related_name="merches_on_shipping",
        verbose_name="ID отправки"
    )
    merch = models.ForeignKey(
        Merch,
        on_delete=models.CASCADE,
        related_name="merches_on_shipping",
        verbose_name="Мерч"
    )
    amount = models.PositiveIntegerField(
        verbose_name="Количество",
        default=1,
        validators=(
            MinValueValidator(
                1,
                message="Укажите количество мерча"
            ),
        )
    )
    size = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Размер мерча"
    )

    class Meta:
        verbose_name = "Мерч в отправке"
        verbose_name_plural = "Мерч в отправке"

    def __str__(self):
        return f"{self.shipping} - {self.merch}"


class Venue(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name="Название площадки"
    )

    class Meta:
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Content(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        related_name="content",
        verbose_name="Амбассадор"
    )
    link = models.URLField(null=True)
    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        related_name="content",
        verbose_name="Площадка"
    )
    date = models.DateField()
    guide_followed = models.BooleanField(
        default=False,
        verbose_name="По гайду да/нет"
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Обновлено"
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        blank=True,
        null=True
    )
    viewed = models.BooleanField(
        default=False,
        verbose_name="Просмотрено/не просмотрено"
    )

    class Meta:
        verbose_name = "Контент амбассадора"
        verbose_name_plural = "Контент амбассадора"
        ordering = ["-date"]

    def __str__(self):
        return (
            f"Амбассадор: {self.ambassador} {self.link}"
        )


class Notification(models.Model):
    text = models.TextField(verbose_name="Текст уведомления")
    created = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        db_index=True
    )
    viewed = models.BooleanField(
        default=False,
        verbose_name="Просмотрено/не просмотрено"
    )

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.text[:15]}"
