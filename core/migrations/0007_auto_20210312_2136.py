# Generated by Django 3.1.7 on 2021-03-12 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210312_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=150, verbose_name='Benefícios')),
            ],
            options={
                'verbose_name': 'Benefício',
                'verbose_name_plural': 'Benefícios',
            },
        ),
        migrations.RemoveField(
            model_name='plan',
            name='description',
        ),
        migrations.AddField(
            model_name='plan',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.benefits'),
        ),
    ]
