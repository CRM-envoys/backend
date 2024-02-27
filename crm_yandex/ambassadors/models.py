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


class Ambassador(models.Model):
    name1 = models.CharField(
        max_length=Limits.DESIGNATION.value,
        verbose_name='Название1',
    )
    fio = models.CharField(max_length=100, verbose_name='ФИО'),
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
        verbose_name = 'Персональные данные'
        verbose_name_plural = 'Персональные данные'


class Recipe(models.Model):
    course = models.ManyToManyField(
        Course,
        related_name='courses2',
        verbose_name='Ссылка на курс'
    )
    name = models.CharField(
        max_length=Limits.DESIGNATION.value,
        verbose_name='Название',
    )
    text = models.TextField(
        verbose_name='Как приготовить'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        default=0,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name
