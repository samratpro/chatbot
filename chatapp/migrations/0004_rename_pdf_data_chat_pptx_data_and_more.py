# Generated by Django 4.2.3 on 2023-08-07 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_alter_chat_pdf_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='pdf_data',
            new_name='pptx_data',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='chatcategory',
            name='pdf_data',
        ),
        migrations.RemoveField(
            model_name='chatcategory',
            name='time',
        ),
    ]
