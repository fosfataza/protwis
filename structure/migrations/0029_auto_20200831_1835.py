# Generated by Django 3.0.3 on 2020-08-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0028_auto_20200829_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structurestabilizingagent',
            name='slug',
            field=models.SlugField(max_length=75, unique=True),
        ),
    ]