# Generated by Django 5.0.6 on 2024-05-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_alter_post_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
