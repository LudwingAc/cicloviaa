# Generated by Django 2.2.4 on 2019-09-15 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A3', '0011_accidentesocurridos_activacionesyproyectosrealizados_eventosrealizados_unidadesdeapoyo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]