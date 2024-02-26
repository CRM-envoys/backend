from django.db import models
from core.constants import Limits


class Course(models.Model):
    name = models.CharField(
        verbose_name='Название курса',
        max_length=Limits.DESIGNATION.value,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Ссылка на курс',
        max_length=Limits.DESIGNATION.value,
        null=True,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Список курсов'
        verbose_name = 'Название курса'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(
        verbose_name='Статус амбассадора',
        max_length=Limits.DESIGNATION.value,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Ссылка на статус амбассадора',
        max_length=Limits.DESIGNATION.value,
        null=True,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Перечень статусов амбассадоров'
        verbose_name = 'Статус амбассадора'

    def __str__(self):
        return self.name


class PersonalInfo(models.Model):
    fio = models.CharField(max_length=100),
    city = models.CharField(max_length=30),
    country = models.CharField(max_length=30),
    course = models.ManyToManyField(
        Course,
        related_name='courses',
        verbose_name='Ссылка на курс'
    )
    promo = models.CharField(max_length=10),
    status = models.SlugField(max_length=10, unique=True),
    status = models.ManyToManyField(
        Status,
        related_name='statuses',
        verbose_name='Статус амбассадора'
    )
    registrationDate = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )

    class Meta:
        ordering = ['-registrationDate']
        verbose_name = 'Персональные данные'
        verbose_name_plural = 'Персональные данные'

    def __str__(self):
        return self.name







"""
class Сontacts(models.Model):
    telegram = models.CharField(max_length=20),
    phoneNumber = models.CharField(max_length=20),
    email = models.EmailField(max_length=20),

    class Meta:
        ordering = ['telegram']
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name
   

class GuideInfo(models.Model):
    guideOneStatus = models.BooleanField(default=False),
    guideOnePlace = models.CharField(max_length=100),
    guideOneUrl = models.CharField(max_lenght=100),
    guideTwoStatus = models.BooleanField(default=False),
    guideTwoFirstPlace = models.CharField(max_lenght=100),
    guideTwoFirstUrl = models.CharField(max_lenght=100),
    guideTwoSecondPlace = models.CharField(max_lenght=100),
    guideTwoSecondUrl = models.CharField(max_lenght=100),
    onboardingStatus = models.BooleanField(default=False),


"""
