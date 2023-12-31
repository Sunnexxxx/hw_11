# Generated by Django 4.2.7 on 2023-11-17 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('course', models.CharField(choices=[('1', '1-й курс'), ('2', '2-й курс'), ('3', '3-й курс')], max_length=2)),
                ('instrument', models.CharField(choices=[('piano', 'Пианино'), ('guitar', 'Гитара'), ('violin', 'Скрипка')], max_length=10)),
                ('performance', models.IntegerField(default=1, help_text='От 1 до 12')),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
    ]
