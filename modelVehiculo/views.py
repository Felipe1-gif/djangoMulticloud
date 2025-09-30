
from modelVehiculo.models import Vehiculo
from django.shortcuts import render,redirect
from . import forms
def index(request):
    form =forms.VehiculoForm()
    if request.method=='POST':
        form=forms.VehiculoForm(request.POST)
        if form.is_valid():
            print("Formulario OK")
            print("Vehiculo: ",form.cleaned_data['vehiculo'])
            #ver información procesada desde el form
            form.save()
            return redirect('vehiculo:vehiculos')
    data={'form':form}
    return render(request,'modelVehiculo/index.html',data)
def listar_vehiculo(request):
   vehiculo = Vehiculo.objects.all()
   data={'vehiculos':vehiculo}  
   return render(request,'modelVehiculo/vehiculo.html',data)

def editar_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(id=id)
    form = forms.VehiculoForm(request.POST, instance=vehiculo)
    if form.is_valid():
         form.save()
    else:
        data={'form':form}
        return render(request,'modeVehiculo/index.html',data)
    
def eliminar_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    return redirect("vehiculo:vehiculos")