# Generated by Django 4.0 on 2021-12-13 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Thread', 'verbose_name_plural': 'Threads'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Commentario', 'verbose_name_plural': 'Commentarios'},
        ),
    ]
