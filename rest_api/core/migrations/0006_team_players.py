# Generated by Django 3.2 on 2022-11-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_gamesession_current_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(related_name='team_players', to='core.Player'),
        ),
    ]
