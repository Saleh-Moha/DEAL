# Generated by Django 4.2 on 2024-03-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compitition', '0006_remove_questions_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
