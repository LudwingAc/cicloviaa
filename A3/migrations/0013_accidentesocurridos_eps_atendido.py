# Generated by Django 2.2.4 on 2019-09-15 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('A3', '0012_eps'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidentesocurridos',
            name='eps_atendido',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='A3.Eps'),
            preserve_default=False,
        ),
    ]
