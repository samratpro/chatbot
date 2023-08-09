# Generated by Django 4.2.3 on 2023-08-07 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0005_chat_name_alter_chat_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='chat',
            name='name',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='output',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='pptx_data',
        ),
        migrations.AlterField(
            model_name='chat',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='ChatCategory',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.chat'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]