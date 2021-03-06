# Generated by Django 3.1.1 on 2020-09-27 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_guia', models.IntegerField()),
                ('cod_medico', models.IntegerField()),
                ('nome_medico', models.TextField(max_length=100)),
                ('data_consulta', models.DateField()),
                ('valor_consulta', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exame', models.TextField(max_length=100)),
                ('valor_exame', models.DecimalField(decimal_places=2, max_digits=5)),
                ('numero_guia_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapes.consulta')),
            ],
        ),
    ]
