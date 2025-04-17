from django.db import models

class LungCancer(models.Model):
    age = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=[(0, 'Feminino'), (1, 'Masculino')], null=True, blank=True)
    smoking = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    finger_discoloration = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    mental_stress = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    exposure_to_pollution = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    long_term_illness = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    energy_level = models.FloatField(null=True, blank=True)
    immune_weakness = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    breathing_issue = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    alcohol_consumption = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    throat_discomfort = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    oxygen_saturation = models.FloatField(null=True, blank=True)
    chest_tightness = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    family_history = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    smoking_family_history = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)
    stress_immune = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], null=True, blank=True)

    def __str__(self):
        return f'Paciente {self.id} - Idade: {self.age} - Gênero: {self.gender}'
