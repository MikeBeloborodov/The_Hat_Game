# Generated by Django 3.2 on 2022-11-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221101_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesession',
            name='current_round',
            field=models.CharField(choices=[('PG', 'Pre game'), ('R1', 'Round 1'), ('R2', 'Round 2'), ('R3', 'Round 3')], default='R1', max_length=2),
        ),
    ]
