# Generated by Django 4.2.2 on 2023-12-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petstore',
            name='category',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
