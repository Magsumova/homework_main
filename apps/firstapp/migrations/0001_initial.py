# Generated by Django 3.2.10 on 2022-05-04 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновление')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаление')),
                ('full_name', models.CharField(max_length=20, verbose_name='Аккаунт')),
                ('description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Акакаунт',
                'verbose_name_plural': 'Аккаунты',
                'ordering': ('full_name',),
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновление')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаление')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновление')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаление')),
                ('age', models.IntegerField(verbose_name='Возраст студета')),
                ('gpa', models.FloatField(verbose_name='Средняя оценка')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='firstapp.account', verbose_name='Аккаунт')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'ordering': ('account',),
            },
        ),
        migrations.CreateModel(
            name='Proffessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновление')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаление')),
                ('full_name', models.CharField(max_length=20, verbose_name='полное имя')),
                ('topic', models.CharField(choices=[{'JAVA', 'Java'}, {'python', 'Python'}, {'JavaScript', 'Typescript'}, {'Ruby', 'TypeScript'}, {'Ruby', 'Goland'}, {'Sql', 'Golang'}, {'swift', 'SQL'}, {'swift', 'Swift'}], default='Java', max_length=20, verbose_name='предмет')),
                ('students', models.ManyToManyField(to='firstapp.Student')),
            ],
            options={
                'verbose_name': 'Проффессор',
                'verbose_name_plural': 'Проффессоры',
                'ordering': ('full_name',),
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновление')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаление')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('subject', models.CharField(max_length=50, verbose_name='Предмет')),
                ('logo', models.ImageField(max_length=255, upload_to='homework/', verbose_name='Логотип')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Домашняя работа',
                'verbose_name_plural': 'Домашние работы',
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновление')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаление')),
                ('title', models.CharField(max_length=100)),
                ('obj', models.FileField(max_length=255, upload_to='homework_files/%Y/%m/%d/', verbose_name='Объект файла')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.homework')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'ordering': ('-datetime_created',),
            },
        ),
    ]
