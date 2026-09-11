from django.shortcuts import render, redirect, get_object_or_404
from .models import Device


def home(request):
    if request.method == 'POST':
        model_name = request.POST.get('model_name')
        imei = request.POST.get('imei_or_serial')
        status = request.POST.get('status')
        custom_status = request.POST.get('custom_status', '')
        price = request.POST.get('purchase_price')

        if model_name and imei and price:
            Device.objects.create(
                model_name=model_name,
                imei_or_serial=imei,
                status=status,
                custom_status=custom_status,
                purchase_price=price
            )
        return redirect('home')

    all_devices = Device.objects.all().order_by('-id')
    return render(request, 'phone/home.html', {'devices': all_devices})


def delete_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    return redirect('home')


def edit_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        device.model_name = request.POST.get('model_name')
        device.imei_or_serial = request.POST.get('imei_or_serial')
        device.status = request.POST.get('status')
        device.custom_status = request.POST.get('custom_status', '')
        device.purchase_price = request.POST.get('purchase_price')
        device.save()
        return redirect('home')
    return render(request, 'phone/edit.html', {'device': device})