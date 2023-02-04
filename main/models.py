from django.core.validators import RegexValidator
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class MaritalStatus(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Семейное положение'
        verbose_name_plural = 'Семейные положения'


class Citizenship(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Гражданство'
        verbose_name_plural = 'Гражданства'


class Disability(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инвалидность'
        verbose_name_plural = 'Инвалидности'


alpha = RegexValidator(r'^[а-яА-Я]*$', 'Данное поле должно состоять исключительно из букв')
passport_number_regex = RegexValidator(r'[0-9]{7}', 'Данное поле должно состоять исключительно из 7 цифр')
phone_number_regex = RegexValidator(r'^[0-9\-\+]{13}$', 'Данное поле должно сосоять из номера телефона начиная с +')


class Client(models.Model):
    first_name = models.CharField(max_length=250, verbose_name='Имя', validators=[alpha])
    surname = models.CharField(max_length=250, verbose_name='Фамилия')
    father_name = models.CharField(max_length=250, verbose_name='Отчество')
    birth_at = models.DateField(verbose_name='Дата рождения')
    passport_series = models.CharField(max_length=10, verbose_name='Серия паспорта')
    passport_number = models.CharField(max_length=9, verbose_name='Номер паспорта', unique=True,
                                       validators=[passport_number_regex])
    passport_issuer = models.CharField(max_length=250, verbose_name='Кем выдан')
    passport_issue_at = models.DateField(verbose_name='Дата выдачи')
    id_number = models.CharField(max_length=100, verbose_name='Идентификационный номер', unique=True)
    birth_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Место рождения',
                                   related_name='birth_city')
    current_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город фактического проживания',
                                     related_name='current_city')
    current_live_address = models.CharField(max_length=250, verbose_name='Адрес фактического проживания')
    home_phone_number = models.CharField(default='', null=True, blank=True, max_length=25,
                                         verbose_name='Телефон домашний', validators=[phone_number_regex])
    mobile_phone_number = models.CharField(default='', null=True, blank=True, max_length=25,
                                           verbose_name='Телефон мобильный', validators=[phone_number_regex])
    email = models.EmailField(default='', null=True, blank=True, verbose_name='Электронная почта')
    work_place = models.CharField(max_length=250, default='', null=True, blank=True, verbose_name='Место работы')
    work_occupation = models.CharField(max_length=250, default='', null=True, blank=True, verbose_name='Должность')
    city_of_residence = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город прописки',
                                          related_name='city_of_residence')
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, verbose_name="Семейное положение")
    citizenship = models.ForeignKey(Citizenship, on_delete=models.CASCADE, verbose_name='Гражданство')
    disability = models.ForeignKey(Disability, on_delete=models.CASCADE, verbose_name='Инвалидность')
    is_retired = models.BooleanField(verbose_name='Пенсионер')
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                         verbose_name='Ежемесячный доход')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        unique_together = ('first_name', 'surname', 'father_name')

    def __str__(self):
        return f'{self.first_name} {self.surname} {self.father_name}'
