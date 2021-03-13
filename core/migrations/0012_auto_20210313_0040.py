# Generated by Django 3.1.7 on 2021-03-13 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_plan_beneficios'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='benefit1',
            field=models.CharField(default='benefício 1', max_length=100, verbose_name='Benefício-1'),
        ),
        migrations.AddField(
            model_name='plan',
            name='benefit2',
            field=models.CharField(default='benefício 2', max_length=100, verbose_name='Benefício-2'),
        ),
        migrations.AddField(
            model_name='plan',
            name='benefit3',
            field=models.CharField(default='benefício 3', max_length=100, verbose_name='Benefício-3'),
        ),
        migrations.AddField(
            model_name='plan',
            name='benefit4',
            field=models.CharField(default='benefício 4', max_length=100, verbose_name='Benefício-4'),
        ),
    ]