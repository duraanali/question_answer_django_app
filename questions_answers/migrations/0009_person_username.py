# Generated by Django 3.0.7 on 2020-06-27 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_answers', '0008_auto_20200627_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
