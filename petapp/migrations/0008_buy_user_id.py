# Generated by Django 4.2.2 on 2024-01-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0007_cart_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='user_id',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]
