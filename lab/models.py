from django.db import models
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import pymysql
pymysql.install_as_MySQLdb()

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название модели автомобиля')
    price = models.FloatField(verbose_name='Цена')
    country = models.CharField(max_length=100, verbose_name='Страна-производитель')
    # image_car = models.ImageField(upload_to='lab/static/lab/images', verbose_name='Изображение модели')
    image_car = models.ImageField(verbose_name='Изображение модели')
    length = models.CharField(max_length=20, verbose_name='Длина автомобиля')
    vehicle_clearance = models.CharField(max_length=15, verbose_name='Клиренс автомобиля')
    max_speed = models.CharField(max_length=15, verbose_name='Максимальная скорость автомобиля')
    average_fuel_consumption = models.CharField(max_length=15, verbose_name='Средний расход топлива в смешанном режиме')
    weight = models.CharField(max_length=15, verbose_name='Масса автомобиля')
    type_of_transmission = models.CharField(max_length=100, verbose_name='Коробка передач')
    volume = models.CharField(max_length=20, verbose_name='Объем двигателя')
    description = models.CharField(max_length=1500, verbose_name='Описание')

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    adr = models.CharField(max_length=255, verbose_name='Адрес')
    time = models.CharField(max_length=255, verbose_name='Время работы')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    image_adr = models.ImageField(verbose_name='Схема проезда:')


class Sales(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    date = models.CharField(max_length=50, verbose_name='Сроки акции')
    text = models.CharField(max_length=255, verbose_name='Описание')


class User1 (models.Model):
    dop_id = models.IntegerField()
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    phone = models.CharField(max_length=20, verbose_name='Контактный телефон')
    email = models.EmailField(verbose_name='Электронная почта')


def __str__(self):
    return self.first_name


#форма для регистрации
class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин:')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль:')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите ввод:')
    email = forms.EmailField(label='Email:')
    first_name = forms.CharField(max_length=30, label='Введите имя:')
    last_name = forms.CharField(max_length=30, label='Введите фамилию:')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('Логин уже занят')
        except User.DoesNotExist:
            return username

    def clean_password2(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['password2']
        if pass1 != pass2:
            raise forms.ValidationError('Пароли не совпадают, введите одинаковые пароли')

    def save(self):
        user = User()
        data = self.cleaned_data
        user.username = data.get('username')
        user.password = make_password(data.get('password'))
        user.email = data.get('email')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.is_active = True
        user.is_superuser = False
        user.save()
        return authenticate(username=user.username, password=user.password)

#форма для авторизации
class AuthorizationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин пользователя:')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль пользователя:')

    def clean(self):
        data = self.cleaned_data
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is not None:
            if user.is_active:
                data['user'] = user
            else:
                raise forms.ValidationError('Пользователь неактивен')
        else:
            raise forms.ValidationError('Неверный логин или пароль')











