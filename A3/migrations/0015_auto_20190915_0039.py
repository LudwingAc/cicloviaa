# Generated by Django 2.2.4 on 2019-09-15 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('A3', '0014_auto_20190915_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidentesocurridos',
            name='eps_atendido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='A3.Eps'),
        ),
    ]
