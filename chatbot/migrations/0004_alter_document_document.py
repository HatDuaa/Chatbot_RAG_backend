# Generated by Django 5.1.3 on 2024-11-14 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_document_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]