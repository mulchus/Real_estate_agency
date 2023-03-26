from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField(
        'Текст объявления',
        blank=True)

    price = models.IntegerField(
        'Цена квартиры',
        db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)

    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')

    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')

    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)

    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField(
        'Наличие балкона',
        default=False,
        db_index=True)

    active = models.BooleanField(
        'Активно-ли объявление',
        default=True,
        db_index=True)

    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    liked_by = models.ManyToManyField(
        User,
        verbose_name='Кто лайкнул',
        related_name='liked_flats',
        null=True,
        blank=True)

    new_building = models.BooleanField(
        'Новостройка ли',
        null=True,
        blank=True,
        db_index=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Owner(models.Model):
    owner = models.CharField(
        'ФИО владельца',
        max_length=200,
        db_index=True)

    owners_phonenumber = models.CharField(
        'Номер владельца',
        max_length=20,
        db_index=True)

    owner_pure_phone = PhoneNumberField(
        verbose_name='Нормализованный номер владельца',
        max_length=20,
        null=True,
        blank=True,
        db_index=True)

    flat = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности',
        related_name='owner_flats',
        db_index=True)


class Claim(models.Model):
    username = models.ForeignKey(
        User,
        verbose_name='Кто жаловался',
        related_name='claims',
        on_delete=models.CASCADE)

    flat = models.ForeignKey(
        Flat,
        verbose_name='Квартира, на которую пожаловались',
        related_name='flats',
        on_delete=models.CASCADE)

    claim_text = models.TextField(
        verbose_name='Текст жалобы',
        max_length=2000)

    def __str__(self):
        return f'{self.username}, {self.flat}'
