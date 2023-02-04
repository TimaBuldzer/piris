# Generated by Django 4.1.5 on 2023-01-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('father_name', models.CharField(max_length=250, verbose_name='Отчество')),
                ('birth_at', models.DateField(verbose_name='Дата рождения')),
                ('passport_series', models.CharField(max_length=10, verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(max_length=9, verbose_name='Номер паспорта')),
                ('passport_issuer', models.CharField(max_length=250, verbose_name='Кем выдан')),
                ('passport_issue_at', models.DateField(verbose_name='Дата выдачи')),
                ('id_number', models.CharField(max_length=100, verbose_name='Идентификационный номер')),
                ('birth_city', models.CharField(max_length=250, verbose_name='Место рождения')),
                ('current_city', models.CharField(max_length=250, verbose_name='Место проживания')),
                ('current_live_address', models.CharField(max_length=250, verbose_name='Адрес фактического проживания')),
                ('home_phone_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон домашний')),
                ('mobile_phone_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон мобильный')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта')),
                ('work_place', models.CharField(blank=True, max_length=250, null=True, verbose_name='Место работы')),
                ('work_occupation', models.CharField(blank=True, max_length=250, null=True, verbose_name='Должность')),
                ('city_of_residence', models.CharField(max_length=250, verbose_name='Город прописки')),
                ('marital_status', models.CharField(choices=[('married', 'Женат/Замужем'), ('divorced', 'Разведен/Разведена'), ('widowed', 'Вдовец/Вдова'), ('not_married', 'Не женат/Не замужем')], max_length=250, verbose_name='Семейно положение')),
                ('citizenship', models.CharField(choices=[('uzbek', 'Узбек'), ('belarussian', 'Белорус'), ('russian', 'Русский')], max_length=250, verbose_name='Гражданство')),
                ('is_disabled', models.CharField(choices=[('not_disabled', 'Инвалидность отсуствует'), ('first_group', 'Первая группа инвалидности'), ('second_group', 'Вторая группа инвалидности'), ('third_group', 'Третья группа инвалидности')], max_length=250, verbose_name='Инвалидность')),
                ('is_retired', models.BooleanField(verbose_name='Пенсионер')),
                ('monthly_income', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Ежемесячный доход')),
            ],
        ),
    ]
