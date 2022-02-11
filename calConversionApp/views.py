from django.shortcuts import render
from django.views.generic import View

MECHANICAL_EQUIVALENT_OF_HEAT = 4.184
SI_PREFIXES = 1000

class ConvView(View):
    def get(self, request):
        context = {
            'cal': '0',
            'joule': '0',
            'onigiri': '0',
            'gasoline': '0',
        }
        return render(request, 'conversion.html', context)

    def post(self, request):
        cal = float(request.POST['cal'])
        joule = round(cal * MECHANICAL_EQUIVALENT_OF_HEAT, 1)
        num_onigiri = round(cal / 180, 1)
        num_gasoline = round(joule / 33360, 1)
        context = {
            'cal': cal,
            'joule': joule,
            'onigiri': num_onigiri,
            'gasoline': num_gasoline,
        }
        return render(request, 'conversion.html', context)

