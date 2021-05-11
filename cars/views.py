from django.shortcuts import render, get_object_or_404
from .models import CarDeal
from mikar9.models import Invoice

# Create( your views here.


def cars(request):
    data = CarDeal.objects.all().order_by('deal_ref')
    car = {
            'deal_ref': 'Not selected',
            'car_plate': 'Not selected',
            'chassis_no': 'Not selected',
            'engine_no': 'Not selected',
            'buyer': 'Not selected',
            'seller': 'Not selected',
            'referral': 'Not selected'
        }
    invoices = [] 

    print(car['car_plate'])
    if request.method == "POST":
        item_id = request.POST.get('carplate')
        if item_id == 'none':
            pass
        else:
            car = get_object_or_404(CarDeal, pk=item_id)
            invoices = Invoice.objects.filter(car_plate=car.car_plate)
    

    return render(request, 'cars.html', {
        'data': data,
        'car': car,
        'invoices': invoices
    })
