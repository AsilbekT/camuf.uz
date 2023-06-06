# Generated by Django 4.1.1 on 2023-06-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('user_step', models.CharField(blank=True, max_length=100)),
                ('user_lang', models.CharField(blank=True, max_length=10)),
                ('user_contact', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
