# Generated by Django 4.2.3 on 2023-08-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0007_rename_message_chatmessage_prompt_chatmessage_replay'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_cookie',
            field=models.TextField(blank=True, null=True),
        ),
    ]
