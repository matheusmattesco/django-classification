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

        data = ControlModels.LungCancer(
            age=data_array[1],
            gender=data_array[0],
            smoking=data_array[2],
            finger_discoloration=data_array[3],
            mental_stress=data_array[4],
            exposure_to_pollution=data_array[5],
            long_term_illness=data_array[6],
            energy_level=data_array[7],
            immune_weakness=data_array[8],
            breathing_issue=data_array[9],
            alcohol_consumption=data_array[10],
            throat_discomfort=data_array[11],
            oxygen_saturation=data_array[12],
            chest_tightness=data_array[13],
            family_history=data_array[14],
            smoking_family_history=data_array[15],
            stress_immune=data_array[16],
            resultado=resultado  
        )
        data.save()

        return render(request, './forms.html', {
            'resultado': resultado,
        })

class LungCancerEdit(View):
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
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

        ControlModels.LungCancer.objects.filter(id=request.POST.get('id')).update(
            gender=data_array[0],
            age=data_array[1],
            smoking=data_array[2],
            finger_discoloration=data_array[3],
            mental_stress=data_array[4],
            exposure_to_pollution=data_array[5],
            long_term_illness=data_array[6],
            energy_level=data_array[7],
            immune_weakness=data_array[8],
            breathing_issue=data_array[9],
            alcohol_consumption=data_array[10],
            throat_discomfort=data_array[11],
            oxygen_saturation=data_array[12],
            chest_tightness=data_array[13],
            family_history=data_array[14],
            smoking_family_history=data_array[15],
            stress_immune=data_array[16],
            resultado=resultado
        )

        return render(request, '../templates/forms.html', {
            'resultado': resultado
        })
    
def load_model():
    path = os.path.join(settings.BASE_DIR, 'ml', 'model.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)

model = load_model()
