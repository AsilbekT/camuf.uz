# Generated by Django 4.1.1 on 2023-05-17 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_new_news_catagory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='articlecatagory',
            options={'verbose_name': 'Article Category', 'verbose_name_plural': 'Article Categories'},
        ),
        migrations.AlterModelOptions(
            name='emailaddress',
            options={'verbose_name': 'University email', 'verbose_name_plural': 'University emails'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterModelOptions(
            name='graduatecourse',
            options={'verbose_name': 'Graduate Course', 'verbose_name_plural': 'Graduate Courses'},
        ),
        migrations.AlterModelOptions(
            name='interestedpeople',
            options={'verbose_name': 'Interested People', 'verbose_name_plural': 'Interested People'},
        ),
        migrations.AlterModelOptions(
            name='leaders',
            options={'verbose_name': 'Leader', 'verbose_name_plural': 'Leaders'},
        ),
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='newscatagory',
            options={'verbose_name': 'News Category', 'verbose_name_plural': 'New Categories'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statues'},
        ),
        migrations.AlterModelOptions(
            name='undergraduatecourse',
            options={'verbose_name': 'Undergraduate Course', 'verbose_name_plural': 'Undergraduate Courses'},
        ),
        migrations.AlterModelOptions(
            name='uniphone',
            options={'verbose_name': 'University Number', 'verbose_name_plural': 'University Numbers'},
        ),
        migrations.AlterModelOptions(
            name='workers',
            options={'verbose_name': 'Worker', 'verbose_name_plural': 'Workers'},
        ),
    ]