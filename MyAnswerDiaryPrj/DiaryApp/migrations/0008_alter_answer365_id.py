# Generated by Django 4.0.6 on 2022-08-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0007_alter_answer365_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer365',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]