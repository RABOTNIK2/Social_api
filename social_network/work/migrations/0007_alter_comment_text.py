# Generated by Django 5.0.6 on 2024-05-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_alter_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
