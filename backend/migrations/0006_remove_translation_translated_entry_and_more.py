# Generated by Django 5.1 on 2024-08-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_translation_entry_remove_translation_meaning_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translation',
            name='translated_entry',
        ),
        migrations.RemoveField(
            model_name='translation',
            name='translated_meaning',
        ),
        migrations.AddField(
            model_name='translation',
            name='entry',
            field=models.CharField(default='', max_length=48),
        ),
        migrations.AddField(
            model_name='translation',
            name='meaning',
            field=models.TextField(default='', max_length=512),
        ),
    ]
