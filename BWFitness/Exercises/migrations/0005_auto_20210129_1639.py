# Generated by Django 3.1.4 on 2021-01-29 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0004_auto_20210129_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='progressionFrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='easier', to='Exercises.exercise'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='progressionTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='harder', to='Exercises.exercise'),
        ),
    ]
