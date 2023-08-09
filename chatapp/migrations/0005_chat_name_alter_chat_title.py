# Generated by Django 4.2.3 on 2023-08-07 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_rename_pdf_data_chat_pptx_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatapp.chatcategory'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='title',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
