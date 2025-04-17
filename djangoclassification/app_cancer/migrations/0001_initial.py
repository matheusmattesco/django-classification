# Generated by Django 5.2 on 2025-04-16 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LungCancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'Feminino'), (1, 'Masculino')])),
                ('smoking', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('finger_discoloration', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('mental_stress', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('exposure_to_pollution', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('long_term_illness', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('energy_level', models.FloatField()),
                ('immune_weakness', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('breathing_issue', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('alcohol_consumption', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('throat_discomfort', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('oxygen_saturation', models.FloatField()),
                ('chest_tightness', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('family_history', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('smoking_family_history', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
                ('stress_imune', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
            ],
        ),
    ]
