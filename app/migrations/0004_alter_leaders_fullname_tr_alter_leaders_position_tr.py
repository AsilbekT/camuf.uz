# Generated by Django 4.1.1 on 2023-06-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_status_about_university_title_tr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaders',
            name='fullname_tr',
            field=models.CharField(default='s', max_length=200),
        ),
        migrations.AlterField(
            model_name='leaders',
            name='position_tr',
            field=models.CharField(default='s', max_length=200),
        ),
    ]