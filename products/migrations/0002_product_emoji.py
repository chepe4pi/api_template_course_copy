# Generated by Django 5.0.2 on 2024-05-24 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='emoji',
            field=models.CharField(max_length=16, null=True),
        ),
    ]