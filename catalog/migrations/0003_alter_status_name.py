# Generated by Django 4.1.3 on 2022-11-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(help_text='Введите статус экземпляра книги', max_length=20, verbose_name='Статус экземпляра книги'),
        ),
    ]
