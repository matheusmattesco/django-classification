from django.db import models

class LungCancerModel(models.Model):
    id = models.AutoField(primary_key=True)
    AGE = models.IntegerField()
    GENDER = models.IntegerField(choices=[(0, 'Feminino'), (1, 'Masculino')])
    SMOKING = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    FINGER_DISCOLORATION = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    MENTAL_STRESS = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    EXPOSURE_TO_POLLUTION = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    LONG_TERM_ILLNESS = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    ENERGY_LEVEL = models.FloatField()
    IMMUNE_WEAKNESS = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    BREATHING_ISSUE = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    ALCOHOL_CONSUMPTION = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    THROAT_DISCOMFORT = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    OXYGEN_SATURATION = models.FloatField()
    CHEST_TIGHTNESS = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    FAMILY_HISTORY = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    SMOKING_FAMILY_HISTORY = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    STRESS_IMMUNE = models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')])

    def __str__(self):
        return f'Paciente {self.id} - Idade: {self.AGE} - Gênero: {self.GENDER}'
    
    class Meta:
        db_table = 'LungCancer'
