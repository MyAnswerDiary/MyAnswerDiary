# Generated by Django 4.0.2 on 2022-08-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0003_alter_question365_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question365',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]