# Generated by Django 5.1 on 2024-08-19 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_word_translations_translation_word'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translation',
            old_name='entry',
            new_name='translated_entry',
        ),
        migrations.RenameField(
            model_name='translation',
            old_name='meaning',
            new_name='translated_meaning',
        ),
        migrations.AddField(
            model_name='translation',
            name='lang',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='backend.word'),
        ),
        migrations.AlterField(
            model_name='word',
            name='entry',
            field=models.CharField(max_length=48, unique=True),
        ),
    ]
