# Generated by Django 5.0.6 on 2024-05-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0007_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reaction',
            field=models.IntegerField(default=0),
        ),
    ]