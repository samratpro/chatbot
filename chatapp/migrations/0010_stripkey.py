# Generated by Django 4.2.3 on 2023-08-11 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0009_openaikey'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=300)),
            ],
        ),
    ]
