# Generated by Django 3.1.4 on 2021-01-31 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0007_auto_20210130_1541'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='exercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='part_of_prog', to='Exercises.exercise', unique=True),
        ),
    ]