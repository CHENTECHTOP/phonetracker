from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Device
from .forms import UserRegisterForm
from django.contrib.auth import login


class HomePageView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        devices = Device.objects.filter(user=request.user).order_by('-id')
        return render(request, 'phone/home.html', {'devices': devices})

    def post(self, request):
        model_name = request.POST.get('model_name')
        imei = request.POST.get('imei_or_serial')
        status = request.POST.get('status')
        custom_status = request.POST.get('custom_status', '')
        price = request.POST.get('purchase_price')

        if model_name and imei and price:
            Device.objects.create(
                user=request.user,
                model_name=model_name,
                imei_or_serial=imei,
                status=status,
                custom_status=custom_status,
                purchase_price=price
            )
        return redirect('home')


class DeviceDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk, user=request.user)
        device.delete()
        return redirect('home')


class DeviceEditView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk, user=request.user)
        return render(request, 'phone/edit.html', {'device': device})

    def post(self, request):
        device = get_object_or_404(Device, pk=pk, user=request.user)
        device.model_name = request.POST.get('model_name')
        device.imei_or_serial = request.POST.get('imei_or_serial')
        device.status = request.POST.get('status')
        device.custom_status = request.POST.get('custom_status', '')
        device.purchase_price = request.POST.get('purchase_price')
        device.save()
        return redirect('home')


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'phone/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'phone/register.html', {'form': form})