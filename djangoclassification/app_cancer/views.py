from django.views import View
from django.shortcuts import render, redirect
import traceback
import pickle
import pandas as pd
import os
from django.conf import settings
from app_cancer.models import LungCancerModel

class LungCancerView(View):
    def get(self, request):
        context = {
            'data_set': LungCancerModel.objects.all()
        }
        return render(request, 'app_cancer/templates/index.html', context=context)

def load_model():
    path = os.path.join(settings.BASE_DIR, 'ml', 'model.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)

model = load_model()

def predict_cancer(request):
    # Dados do DataFrame para pré-preenchimento
    novo_dado = {
        "AGE": 58,
        "GENDER": 1,
        "SMOKING": 1,
        "FINGER_DISCOLORATION": 1,
        "MENTAL_STRESS": 0,
        "EXPOSURE_TO_POLLUTION": 1,
        "LONG_TERM_ILLNESS": 1,
        "ENERGY_LEVEL": 0,
        "IMMUNE_WEAKNESS": 1,
        "BREATHING_ISSUE": 1,
        "ALCOHOL_CONSUMPTION": 0,
        "THROAT_DISCOMFORT": 1,
        "OXYGEN_SATURATION": 1,
        "CHEST_TIGHTNESS": 1,
        "FAMILY_HISTORY": 1,
        "SMOKING_FAMILY_HISTORY": 1,
        "STRESS_IMMUNE": 1
    }
    
    resultado = None
    if request.method == 'POST':
        try:
            data = [
                int(request.POST.get('GENDER')),
                int(request.POST.get('AGE')),
                int(request.POST.get('SMOKING')),
                int(request.POST.get('FINGER_DISCOLORATION')),
                int(request.POST.get('MENTAL_STRESS')),
                int(request.POST.get('EXPOSURE_TO_POLLUTION')),
                int(request.POST.get('LONG_TERM_ILLNESS')),
                float(request.POST.get('ENERGY_LEVEL')),
                int(request.POST.get('IMMUNE_WEAKNESS')),
                int(request.POST.get('BREATHING_ISSUE')),
                int(request.POST.get('ALCOHOL_CONSUMPTION')),
                int(request.POST.get('THROAT_DISCOMFORT')),
                float(request.POST.get('OXYGEN_SATURATION')),
                int(request.POST.get('CHEST_TIGHTNESS')),
                int(request.POST.get('FAMILY_HISTORY')),
                int(request.POST.get('SMOKING_FAMILY_HISTORY')),
                int(request.POST.get('STRESS_IMMUNE')),
            ]

            prediction = model.predict([data])[0]
            resultado = 'Com câncer' if prediction == 1 else 'Sem câncer'
        except Exception as e:
            resultado = f'Erro na previsão: {e}'
    
    return render(request, './forms.html', {
        'resultado': resultado,
        'form_data': novo_dado
    })