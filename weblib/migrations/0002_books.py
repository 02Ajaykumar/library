# Generated by Django 3.2.8 on 2024-01-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
