# Generated by Django 4.0.6 on 2022-08-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question365',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=60)),
                ('category', models.CharField(max_length=10)),
                ('num', models.IntegerField()),
            ],
        ),
    ]
