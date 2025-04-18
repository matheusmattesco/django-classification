from django.views import View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.conf import settings
from .models import LungCancer
import app_cancer.models as ControlModels
import os
import pickle
from django.shortcuts import render
from .models import LungCancer

def load_model():
    path = os.path.join(settings.BASE_DIR, 'ml', 'model.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)

model = load_model()


class LungCancerView(View):
    def get(self, request, *args, **kwargs):
        data = ControlModels.LungCancer.objects.all().order_by('id')
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'index.html', {"page_obj": page_obj})
    
class LungCancerRegister(View):
    def get(self, request, *args, **kwargs):
        return render(request, '../templates/forms.html')
    
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        data_array = self._extract_form_data(request)
        prediction = model.predict([data_array])[0]
        resultado = 'Com câncer' if prediction == 1 else 'Sem câncer'

        ControlModels.LungCancer.objects.create(
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
            
        return render(request, '../templates/forms.html', {'resultado': resultado})

    def _extract_form_data(self, request):
        return [
            request.POST.get('gender'),
            request.POST.get('age'),
            request.POST.get('smoking'),
            request.POST.get('finger_discoloration'),
            request.POST.get('mental_stress'),
            request.POST.get('exposure_to_pollution'),
            request.POST.get('long_term_illness'),
            request.POST.get('energy_level'),
            request.POST.get('immune_weakness'),
             request.POST.get('breathing_issue'),
            request.POST.get('alcohol_consumption'),
            request.POST.get('throat_discomfort'),
            request.POST.get('oxygen_saturation'),
            request.POST.get('chest_tightness'),
            request.POST.get('family_history'),
            request.POST.get('smoking_family_history'),
            request.POST.get('stress_immune')
        ]
    

class LungCancerEdit(View):
    @method_decorator(csrf_protect)
    def get(self, request, id, *args, **kwargs):
        data = LungCancer.objects.get(id=id)
        return render(request, 'edit.html', {'data': data})
    
    @method_decorator(csrf_protect)
    def extract_form_data(self, request):
        data = [
            request.POST.get('gender'),
            request.POST.get('age'),
            request.POST.get('smoking'),
            request.POST.get('finger_discoloration'),
            request.POST.get('mental_stress'),
            request.POST.get('exposure_to_pollution'),
            request.POST.get('long_term_illness'),
            request.POST.get('energy_level'),
            request.POST.get('immune_weakness'),
            request.POST.get('breathing_issue'),
            request.POST.get('alcohol_consumption'),
            request.POST.get('throat_discomfort'),
            request.POST.get('oxygen_saturation'),
            request.POST.get('chest_tightness'),
            request.POST.get('family_history'),
            request.POST.get('smoking_family_history'),
            request.POST.get('stress_immune')
        ]
        return data

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        data_array = self.extract_form_data(request)

        prediction = model.predict([data_array])[0]
        resultado = 'Com câncer' if prediction == 1 else 'Sem câncer'

        lung_cancer_instance = ControlModels.LungCancer.objects.get(id=request.POST.get('id'))

        lung_cancer_instance.gender = data_array[0]
        lung_cancer_instance.age = data_array[1]
        lung_cancer_instance.smoking = data_array[2]
        lung_cancer_instance.finger_discoloration = data_array[3]
        lung_cancer_instance.mental_stress = data_array[4]
        lung_cancer_instance.exposure_to_pollution = data_array[5]
        lung_cancer_instance.long_term_illness = data_array[6]
        lung_cancer_instance.energy_level = data_array[7]
        lung_cancer_instance.immune_weakness = data_array[8]
        lung_cancer_instance.breathing_issue = data_array[9]
        lung_cancer_instance.alcohol_consumption = data_array[10]
        lung_cancer_instance.throat_discomfort = data_array[11]
        lung_cancer_instance.oxygen_saturation = data_array[12]
        lung_cancer_instance.chest_tightness = data_array[13]
        lung_cancer_instance.family_history = data_array[14]
        lung_cancer_instance.smoking_family_history = data_array[15]
        lung_cancer_instance.stress_immune = data_array[16]
        lung_cancer_instance.resultado = resultado

        lung_cancer_instance.save()

        return render(request, 'edit.html', {'data': lung_cancer_instance, 'resultado': resultado})


class LungCancerDelete(View):
    def post(self, request, id):
        data = LungCancer.objects.get(id=id)
        data.delete() 

        return redirect('list')