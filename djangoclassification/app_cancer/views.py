from django.views import View
from django.shortcuts import render
import traceback
from django.shortcuts import redirect
import pickle
import pandas as pd
import os
from django.conf import settings


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
            # Coleta os 17 campos do formulário
            data = [
                int(request.POST.get('GENDER')),
                int(request.POST.get('AGE')),
                int(request.POST.get('SMOKING')),
                int(request.POST.get('FINGER_DISCOLORATION')),
                int(request.POST.get('MENTAL_STRESS')),
                int(request.POST.get('EXPOSURE_TO_POLLUTION')),
                int(request.POST.get('LONG_TERM_ILLNESS')),
                int(request.POST.get('ENERGY_LEVEL')),
                int(request.POST.get('IMMUNE_WEAKNESS')),
                int(request.POST.get('BREATHING_ISSUE')),
                int(request.POST.get('ALCOHOL_CONSUMPTION')),
                int(request.POST.get('THROAT_DISCOMFORT')),
                int(request.POST.get('OXYGEN_SATURATION')),
                int(request.POST.get('CHEST_TIGHTNESS')),
                int(request.POST.get('FAMILY_HISTORY')),
                int(request.POST.get('SMOKING_FAMILY_HISTORY')),
                int(request.POST.get('STRESS_IMMUNE')),
            ]
            # Faz a previsão com o modelo
            prediction = model.predict([data])[0]
            resultado = 'Com câncer' if prediction == 1 else 'Sem câncer'
        except Exception as e:
            resultado = f'Erro na previsão: {e}'
    
    # Passa os dados do DataFrame para o template
    return render(request, './forms.html', {
        'resultado': resultado,
        'form_data': novo_dado
    })