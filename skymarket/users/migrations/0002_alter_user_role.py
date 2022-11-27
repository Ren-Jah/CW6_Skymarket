# Generated by Django 3.2.6 on 2022-11-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('USR', 'user'), ('ADM', 'admin')], default='USR', max_length=20),
        ),
    ]
