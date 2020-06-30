# Generated by Django 3.0.7 on 2020-06-28 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions_answers', '0009_person_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='question_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answerByQuestion', to='questions_answers.Questions'),
        ),
    ]
