from django.shortcuts import render
from django.views.generic import View

MECHANICAL_EQUIVALENT_OF_HEAT = 4.184
CAL_ONIGIRI = 180
CAL_GASOLINE = 33360
CAL_BANANA = 86
CAL_SYOKUPAN = 168
CAL_GYUNYU = 641

class ConvView(View):
    def get(self, request):
        context = {
            'cal': '0',
            'joule': '0',
            'onigiri': '0',
            'gasoline': '0',
            'banana': '0',
            'syokupan': '0',
            'gyunyu': '0',
        }
        return render(request, 'conversion.html', context)

    def post(self, request):
        try:
            cal = float(request.POST['cal'])
        except:
            context = {
                'error': "カロリーは数字で入力してください",
            } 
            return render(request, 'conversion.html', context)
        else:
            joule = round(cal * MECHANICAL_EQUIVALENT_OF_HEAT, 1)
            num_onigiri = round(cal / CAL_ONIGIRI, 1)
            num_gasoline = round(joule / CAL_GASOLINE, 1)
            num_banana = round(cal / CAL_BANANA, 1)
            num_syokupan = round(cal / CAL_SYOKUPAN , 1)
            num_gyunyu = round(cal / CAL_GYUNYU, 1)
            context = {
                'cal': cal,
                'joule': joule,
                'onigiri': num_onigiri,
                'gasoline': num_gasoline,
                'banana': num_banana,
                'syokupan': num_syokupan,
                'gyunyu': num_gyunyu,
            }
            return render(request, 'conversion.html', context)

