# Generated by Django 5.0.6 on 2024-05-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_alter_post_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reaction',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]