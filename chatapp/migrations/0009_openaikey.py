# Generated by Django 4.2.3 on 2023-08-10 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0008_chat_chat_cookie'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenAIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=300)),
            ],
        ),
    ]
