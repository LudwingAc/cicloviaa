# Generated by Django 2.2.4 on 2019-08-28 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('A3', '0005_auto_20190827_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='corredor',
            name='tipo_de_corredor',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='A3.TipoDeCorredor'),
            preserve_default=False,
        ),
    ]
