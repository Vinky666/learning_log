# Generated by Django 3.0.9 on 2020-08-06 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='topicId',
            new_name='topic',
        ),
    ]