# Generated by Django 5.1 on 2024-08-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_alter_word_source copy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='source',
            field=models.CharField(max_length=64),
        ),
    ]
