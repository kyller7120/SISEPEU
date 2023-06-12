# Generated by Django 3.2.19 on 2023-05-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_egreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egreso',
            name='anio',
            field=models.IntegerField(verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='egreso',
            name='cantidad',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='egreso',
            name='carrera',
            field=models.CharField(max_length=200, verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='egreso',
            name='facultad',
            field=models.CharField(max_length=200, verbose_name='Facultad'),
        ),
        migrations.AlterField(
            model_name='egreso',
            name='universidad',
            field=models.CharField(max_length=200, verbose_name='Universidad'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='anio',
            field=models.IntegerField(verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='cantidad',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='carrera',
            field=models.CharField(max_length=200, verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='facultad',
            field=models.CharField(max_length=200, verbose_name='Facultad'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='universidad',
            field=models.CharField(max_length=200, verbose_name='Universidad'),
        ),
    ]
