# Generated by Django 4.2.2 on 2023-12-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0002_petstore_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pet_id', models.CharField(max_length=122, null=True)),
                ('name', models.CharField(max_length=122, null=True)),
                ('line', models.CharField(max_length=122, null=True)),
                ('img1', models.TextField(null=True)),
            ],
        ),
    ]
