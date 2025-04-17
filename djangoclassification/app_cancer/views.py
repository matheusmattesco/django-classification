from django.views import View
from django.shortcuts import render, redirect
import traceback
import pickle
import pandas as pd
import os
from django.conf import settings
import app_cancer.models as ControlModels
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


class LungCancerView(View):
    def get(self, request, *args, **kwargs):
        data_frame = ControlModels.LungCancer.objects.all().order_by('id')
        paginator = Paginator(data_frame, 10)  # 10 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, '../templates/index.html', {"page_obj": page_obj})
    
class LungCancerRegister(View):
    def get(self, request, *args, **kwargs):
        return render(request, '../templates/forms.html')
    
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):  
        resultado = None
        data = ControlModels.LungCancer(
            age = int(request.POST.get('age')),
            gender = int(request.POST.get('gender')),
            smoking = int(request.POST.get('smoking')),
            finger_discoloration = int(request.POST.get('finger_discoloration')),
            mental_stress = int(request.POST.get('mental_stress')),
            exposure_to_pollution = int(request.POST.get('exposure_to_pollution')),
            long_term_illness = int(request.POST.get('long_term_illness')),
            energy_level = float(request.POST.get('energy_level')),
            immune_weakness = int(request.POST.get('immune_weakness')),
            breathing_issue = int(request.POST.get('breathing_issue')),
            alcohol_consumption = int(request.POST.get('alcohol_consumption')),
            throat_discomfort = request.POST.get('throat_discomfort'),
            oxygen_saturation = float(request.POST.get('oxygen_saturation')),
            chest_tightness = int(request.POST.get('chest_tightness')),
            family_history = int(request.POST.get('family_history')),
            smoking_family_history = int(request.POST.get('smoking_family_history')),
            stress_immune = int(request.POST.get('stress_immune')),
        )
        data.save()

        data_array = [
            int(request.POST.get('gender')),
            int(request.POST.get('age')),
            int(request.POST.get('smoking')),
            int(request.POST.get('finger_discoloration')),
            int(request.POST.get('mental_stress')),
            int(request.POST.get('exposure_to_pollution')),
            int(request.POST.get('long_term_illness')),
            float(request.POST.get('energy_level')),
            int(request.POST.get('immune_weakness')),
            int(request.POST.get('breathing_issue')),
            int(request.POST.get('alcohol_consumption')),
            int(request.POST.get('throat_discomfort')),
            float(request.POST.get('oxygen_saturation')),
            int(request.POST.get('chest_tightness')),
            int(request.POST.get('family_history')),
            int(request.POST.get('smoking_family_history')),
            int(request.POST.get('stress_immune')),
        ]
                    
        prediction = model.predict([data_array])[0]
        resultado = 'Com câncer' if prediction == 1 else 'Sem câncer'

        return render(request, './forms.html', {
            'resultado': resultado,
        })



class LungCancerEdit(View):
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        ControlModels.LungCancer.objects.filter(id=request.POST.get('id')).update(
            
        )

def load_model():
    path = os.path.join(settings.BASE_DIR, 'ml', 'model.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)

model = load_model()
