from django.shortcuts import render
from django.views.generic import View

MECHANICAL_EQUIVALENT_OF_HEAT = 4.184


class ConvView(View):
    def get(self, request):
        context = {
            'cal': '0',
            'joule': '0',
        }
        return render(request, 'conversion.html', context)

    def post(self, request):
        cal = float(request.POST['cal'])
        joule = cal * MECHANICAL_EQUIVALENT_OF_HEAT
        context = {
            'cal': cal,
            'joule': joule,
        }
        return render(request, 'conversion.html', context)

