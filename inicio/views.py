from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Matricula
from .models import Egreso
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages

def AsignarUniversidad(universidad):
    if(universidad=="uni1"):
            universidad = "Universidad Albert Einstein"
    elif(universidad=="uni2"):
            universidad = "Universidad Autónoma De Santa Ana"
    elif(universidad=="uni3"):
            universidad = "Universidad Capitán General Gerardo Barrios"
    elif(universidad=="uni4"):
            universidad = "Universidad Católica de El Salvador"
    elif(universidad=="uni5"):
            universidad = "Universidad Centroamericana José Simeon Cañas"
    elif(universidad=="uni6"):
            universidad = "Universidad De El Salvador"
    elif(universidad=="uni7"):
            universidad = "Universidad Tecnológica"
    return universidad

################# VISTAS DE USUARIO ##############
def inicio(request):
    return render(request, 'usuario/index.html')

def conseguirCantidad(anio, universidad):

    matriculados = Matricula.objects.all()
    uniCantidad=0
    uni = matriculados.filter(anio = anio, universidad = universidad)
    if(uni):
        for i in uni:
            uniCantidad += i.cantidad
    else:
        uniCantidad = 0
    return uniCantidad

def conseguirCantidadE(anio, universidad):

    egresados = Egreso.objects.all()
    uniCantidad=0
    uni = egresados.filter(anio = anio, universidad = universidad)
    if(uni):
        for i in uni:
            uniCantidad += i.cantidad
    else:
        uniCantidad = 0
    return uniCantidad

def grafico(request):
    cantUni1_m2020 = conseguirCantidad(2020, "Universidad Albert Einstein")
    cantUni1_m2021 = conseguirCantidad(2021, "Universidad Albert Einstein")
    cantUni1_m2022 = conseguirCantidad(2022, "Universidad Albert Einstein")
    cantUni1_mTotal = cantUni1_m2020 + cantUni1_m2021 + cantUni1_m2022

    cantUni2_m2020 = conseguirCantidad(2020, "Universidad Autónoma De Santa Ana")
    cantUni2_m2021 = conseguirCantidad(2021, "Universidad Autónoma De Santa Ana")
    cantUni2_m2022 = conseguirCantidad(2022, "Universidad Autónoma De Santa Ana")
    cantUni2_mTotal = cantUni2_m2020 + cantUni2_m2021 + cantUni2_m2022

    cantUni3_m2020 = conseguirCantidad(2020, "Universidad Capitán General Gerardo Barrios")
    cantUni3_m2021 = conseguirCantidad(2021, "Universidad Capitán General Gerardo Barrios")
    cantUni3_m2022 = conseguirCantidad(2022, "Universidad Capitán General Gerardo Barrios")
    cantUni3_mTotal = cantUni3_m2020 + cantUni3_m2021 + cantUni3_m2022

    cantUni4_m2020 = conseguirCantidad(2020, "Universidad Católica de El Salvador")
    cantUni4_m2021 = conseguirCantidad(2021, "Universidad Católica de El Salvador")
    cantUni4_m2022 = conseguirCantidad(2022, "Universidad Católica de El Salvador")
    cantUni4_mTotal = cantUni4_m2020 + cantUni4_m2021 + cantUni4_m2022

    cantUni5_m2020 = conseguirCantidad(2020, "Universidad Centroamericana José Simeon Cañas")
    cantUni5_m2021 = conseguirCantidad(2021, "Universidad Centroamericana José Simeon Cañas")
    cantUni5_m2022 = conseguirCantidad(2022, "Universidad Centroamericana José Simeon Cañas")
    cantUni5_mTotal = cantUni5_m2020 + cantUni5_m2021 + cantUni5_m2022

    cantUni6_m2020 = conseguirCantidad(2020, "Universidad De El Salvador")
    cantUni6_m2021 = conseguirCantidad(2021, "Universidad De El Salvador")
    cantUni6_m2022 = conseguirCantidad(2022, "Universidad De El Salvador")
    cantUni6_mTotal = cantUni6_m2020 + cantUni6_m2021 + cantUni6_m2022

    cantUni7_m2020 = conseguirCantidad(2020, "Universidad Tecnológica")
    cantUni7_m2021 = conseguirCantidad(2021, "Universidad Tecnológica")
    cantUni7_m2022 = conseguirCantidad(2022, "Universidad Tecnológica")
    cantUni7_mTotal = cantUni7_m2020 + cantUni7_m2021 + cantUni7_m2022

    ###############
    cantUni1_e2020 = conseguirCantidadE(2020, "Universidad Albert Einstein")
    cantUni1_e2021 = conseguirCantidadE(2021, "Universidad Albert Einstein")
    cantUni1_e2022 = conseguirCantidadE(2022, "Universidad Albert Einstein")
    cantUni1_eTotal = cantUni1_e2020 + cantUni1_e2021 + cantUni1_e2022

    cantUni2_e2020 = conseguirCantidadE(2020, "Universidad Autónoma De Santa Ana")
    cantUni2_e2021 = conseguirCantidadE(2021, "Universidad Autónoma De Santa Ana")
    cantUni2_e2022 = conseguirCantidadE(2022, "Universidad Autónoma De Santa Ana")
    cantUni2_eTotal = cantUni2_e2020 + cantUni2_e2021 + cantUni2_e2022

    cantUni3_e2020 = conseguirCantidadE(2020, "Universidad Capitán General Gerardo Barrios")
    cantUni3_e2021 = conseguirCantidadE(2021, "Universidad Capitán General Gerardo Barrios")
    cantUni3_e2022 = conseguirCantidadE(2022, "Universidad Capitán General Gerardo Barrios")
    cantUni3_eTotal = cantUni3_e2020 + cantUni3_e2021 + cantUni3_e2022

    cantUni4_e2020 = conseguirCantidadE(2020, "Universidad Católica de El Salvador")
    cantUni4_e2021 = conseguirCantidadE(2021, "Universidad Católica de El Salvador")
    cantUni4_e2022 = conseguirCantidadE(2022, "Universidad Católica de El Salvador")
    cantUni4_eTotal = cantUni4_e2020 + cantUni4_e2021 + cantUni4_e2022

    cantUni5_e2020 = conseguirCantidadE(2020, "Universidad Centroamericana José Simeon Cañas")
    cantUni5_e2021 = conseguirCantidadE(2021, "Universidad Centroamericana José Simeon Cañas")
    cantUni5_e2022 = conseguirCantidadE(2022, "Universidad Centroamericana José Simeon Cañas")
    cantUni5_eTotal = cantUni5_e2020 + cantUni5_e2021 + cantUni5_e2022

    cantUni6_e2020 = conseguirCantidadE(2020, "Universidad De El Salvador")
    cantUni6_e2021 = conseguirCantidadE(2021, "Universidad De El Salvador")
    cantUni6_e2022 = conseguirCantidadE(2022, "Universidad De El Salvador")
    cantUni6_eTotal = cantUni6_e2020 + cantUni6_e2021 + cantUni6_e2022

    cantUni7_e2020 = conseguirCantidadE(2020, "Universidad Tecnológica")
    cantUni7_e2021 = conseguirCantidadE(2021, "Universidad Tecnológica")
    cantUni7_e2022 = conseguirCantidadE(2022, "Universidad Tecnológica")
    cantUni7_eTotal = cantUni7_e2020 + cantUni7_e2021 + cantUni7_e2022

    context = {
    'cantUni1_m2020': cantUni1_m2020,
    'cantUni1_m2021': cantUni1_m2021,
    'cantUni1_m2022': cantUni1_m2022,
    'cantUni2_m2020': cantUni2_m2020,
    'cantUni2_m2021': cantUni2_m2021,
    'cantUni2_m2022': cantUni2_m2022,
    'cantUni3_m2020': cantUni3_m2020,
    'cantUni3_m2021': cantUni3_m2021,
    'cantUni3_m2022': cantUni3_m2022,
    'cantUni4_m2020': cantUni4_m2020,
    'cantUni4_m2021': cantUni4_m2021,
    'cantUni4_m2022': cantUni4_m2022,
    'cantUni5_m2020': cantUni5_m2020,
    'cantUni5_m2021': cantUni5_m2021,
    'cantUni5_m2022': cantUni5_m2022,
    'cantUni6_m2020': cantUni6_m2020,
    'cantUni6_m2021': cantUni6_m2021,
    'cantUni6_m2022': cantUni6_m2022,
    'cantUni7_m2020': cantUni7_m2020,
    'cantUni7_m2021': cantUni7_m2021,
    'cantUni7_m2022': cantUni7_m2022,
    'cantUni1_mTotal': cantUni1_mTotal,
    'cantUni2_mTotal': cantUni2_mTotal,
    'cantUni3_mTotal': cantUni3_mTotal,
    'cantUni4_mTotal': cantUni4_mTotal,
    'cantUni5_mTotal': cantUni5_mTotal,
    'cantUni6_mTotal': cantUni6_mTotal,
    'cantUni7_mTotal': cantUni7_mTotal,

    'cantUni1_e2020': cantUni1_e2020,
    'cantUni1_e2021': cantUni1_e2021,
    'cantUni1_e2022': cantUni1_e2022,
    'cantUni2_e2020': cantUni2_e2020,
    'cantUni2_e2021': cantUni2_e2021,
    'cantUni2_e2022': cantUni2_e2022,
    'cantUni3_e2020': cantUni3_e2020,
    'cantUni3_e2021': cantUni3_e2021,
    'cantUni3_e2022': cantUni3_e2022,
    'cantUni4_e2020': cantUni4_e2020,
    'cantUni4_e2021': cantUni4_e2021,
    'cantUni4_e2022': cantUni4_e2022,
    'cantUni5_e2020': cantUni5_e2020,
    'cantUni5_e2021': cantUni5_e2021,
    'cantUni5_e2022': cantUni5_e2022,
    'cantUni6_e2020': cantUni6_e2020,
    'cantUni6_e2021': cantUni6_e2021,
    'cantUni6_e2022': cantUni6_e2022,
    'cantUni7_e2020': cantUni7_e2020,
    'cantUni7_e2021': cantUni7_e2021,
    'cantUni7_e2022': cantUni7_e2022,
    'cantUni1_eTotal': cantUni1_eTotal,
    'cantUni2_eTotal': cantUni2_eTotal,
    'cantUni3_eTotal': cantUni3_eTotal,
    'cantUni4_eTotal': cantUni4_eTotal,
    'cantUni5_eTotal': cantUni5_eTotal,
    'cantUni6_eTotal': cantUni6_eTotal,
    'cantUni7_eTotal': cantUni7_eTotal,
}

    return render(request, 'usuario/graficos.html', context)

def resumenes(request):
    return render(request, 'usuario/resumenes.html')

def opcion(request):
    return render(request, 'usuario/opcion.html')

def matriculados(request):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        universidad = request.POST.get('universidad')
        facultad = request.POST.get('facultad')
        carrera = request.POST.get('carrera')
        universidad = AsignarUniversidad(universidad)
        
        matriculas = Matricula.objects.all()
        if((anio == "") and (universidad == "") and (facultad == "") and (carrera == "" )):
            matriculas = Matricula.objects.all()
        elif((not anio == "") and (universidad == "") and (facultad == "") and (carrera == "" )):
            matriculas = matriculas.filter(anio=anio)
        elif((not anio == "") and (not universidad == "") and (facultad == "") and (carrera == "" )):
            matriculas = matriculas.filter(anio=anio, universidad=universidad)
        elif((not anio == "") and (not universidad == "") and (not facultad == "") and (carrera == "" )):
            matriculas = matriculas.filter(anio=anio, universidad=universidad, facultad=facultad)
        elif((not anio == "") and (not universidad == "") and (not facultad == "") and (not carrera == "" )):
            matriculas = matriculas.filter(anio=anio, universidad=universidad, facultad=facultad, carrera=carrera)

        datos = {
            'lista': matriculas
        }
    else:
        matriculas = Matricula.objects.all().order_by('universidad')
        datos = {
            'lista': matriculas,
            'titulo': 'Lista matriculados',
        }
    return render(request, 'usuario/tabla_matriculados.html', datos)

def egresados(request):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        universidad = request.POST.get('universidad')
        facultad = request.POST.get('facultad')
        carrera = request.POST.get('carrera')
        universidad = AsignarUniversidad(universidad)

        egresos = Egreso.objects.all()
        if((anio == "") and (universidad == "") and (facultad == "") and (carrera == "" )):
            egresos = Egreso.objects.all()
        elif((not anio == "") and (universidad == "") and (facultad == "") and (carrera == "" )):
            egresos = egresos.filter(anio=anio)
        elif((not anio == "") and (not universidad == "") and (facultad == "") and (carrera == "" )):
            egresos = egresos.filter(anio=anio, universidad=universidad)
        elif((not anio == "") and (not universidad == "") and (not facultad == "") and (carrera == "" )):
            egresos = egresos.filter(anio=anio, universidad=universidad, facultad=facultad)
        elif((not anio == "") and (not universidad == "") and (not facultad == "") and (not carrera == "" )):
            egresos = egresos.filter(anio=anio, universidad=universidad, facultad=facultad, carrera=carrera)

        datos = {
            'lista': egresos
        }
    else:
        datos = {
            'lista': Egreso.objects.all().order_by('universidad'),
            'titulo': 'Lista egresados',
        }
    return render(request, 'usuario/tabla_egresados.html', datos)

################ VISTAS ADMINISTRADOR ####################
@login_required
def gestion(request):
    return render(request, 'administrador/gestion.html')

@login_required
def egreso(request):
    return render(request, 'administrador/egreso.html')

def logout_view(request):
    logout(request)
    return redirect('/')

###################### CRUD MATRICULA ######################
@login_required
def matricula(request):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        universidad = request.POST.get('universidad')
        facultad = request.POST.get('facultad')
        carrera = request.POST.get('carrera')
        universidad = AsignarUniversidad(universidad)

        matriculas = Matricula.objects.all()
        
        if((anio == "") and (universidad == "") and (facultad == "") and (carrera == "" )):
            matriculas = Matricula.objects.all()
        elif((not anio == "") and (universidad == "") and (facultad == "") and (carrera == "" )):
            matriculas = matriculas.filter(anio=anio)
        elif((not anio == "") and (not universidad == "") and (facultad == "") and (carrera == "" )):
            matriculas = matriculas.filter(anio=anio, universidad=universidad)
        elif((not anio == "") and (not universidad == "") and (not facultad == "") and (carrera == "" )):
            matriculas = matriculas.filter(anio=anio, universidad=universidad, facultad=facultad)
        elif((not anio == "") and (not universidad == "") and (not facultad == "") and (not carrera == "" )):
            matriculas = matriculas.filter(anio=anio, universidad=universidad, facultad=facultad, carrera=carrera)

        datos = {
            'lista': matriculas
        }
    else:
        matriculas = Matricula.objects.all().order_by('universidad')
        datos = {
            'lista': matriculas,
            'titulo': 'Lista matriculas',
        }
    return render(request, 'administrador/matricula.html', datos)

@method_decorator(login_required, name='dispatch')
class CrearMatricula(CreateView):
    template_name = 'administrador/crud_matricula/crear.html'
    model = Matricula
    fields = ['anio', 'universidad', 'facultad', 'carrera', 'cantidad']
    success_url = reverse_lazy('info_app:matricula')

@login_required
def guardar_matricula(request):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        universidad = request.POST.get('universidad')
        facultad = request.POST.get('facultad')
        carrera = request.POST.get('carrera')
        cantidad = request.POST.get('cantidad')

        universidad = AsignarUniversidad(universidad)

        matricula = Matricula(anio=anio, universidad=universidad, facultad=facultad, carrera=carrera, cantidad=cantidad)
        matricula.save()
        return redirect('/matricula')

@login_required
def modificar_matricula(request, pk):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        universidad = request.POST.get('universidad')
        facultad = request.POST.get('facultad')
        carrera = request.POST.get('carrera')
        cantidad = request.POST.get('cantidad')

        universidad = AsignarUniversidad(universidad)

        matricula = Matricula.objects.get(id=pk)
        matricula.anio = anio
        matricula.universidad = universidad
        matricula.facultad = facultad
        matricula.carrera = carrera
        matricula.cantidad = cantidad
        matricula.save()

        return redirect('/matricula')

    matricula = Matricula.objects.get(id=pk)
    return render(request, 'administrador/crud_matricula/modificar.html', {'matricula': matricula})

@login_required
def eliminar_matricula(request, pk):
    matricula = Matricula.objects.get(id=pk)
    matricula.delete()
    messages.success(request, 'La matrícula ha sido eliminada exitosamente.')
    return redirect('info_app:matricula')

########################### CRUD EGRESOS ##########################
@login_required
def guardar_egreso(request):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        universidad = request.POST.get('universidad')
        facultad = request.POST.get('facultad')
        carrera = request.POST.get('carrera')
        cantidad = request.POST.get('cantidad')

        universidad = AsignarUniversidad(universidad)

        egreso = Egreso(anio=anio, universidad=universidad, facultad=facultad, carrera=carrera, cantidad=cantidad)
        egreso.save()
        return redirect('/egreso')

@login_required
def modificar_egreso(request, pk):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        universidad = request.POST.get('universidad')
        facultad = request.POST.get('facultad')
        carrera = request.POST.get('carrera')
        cantidad = request.POST.get('cantidad')

        universidad = AsignarUniversidad(universidad)

        egreso = Egreso.objects.get(id=pk)
        egreso.anio = anio
        egreso.universidad = universidad
        egreso.facultad = facultad
        egreso.carrera = carrera
        egreso.cantidad = cantidad
        egreso.save()

        return redirect('/egreso')

    egreso = Egreso.objects.get(id=pk)
    return render(request, 'administrador/crud_egreso/modificar.html', {'egreso': egreso})

@method_decorator(login_required, name='dispatch')
class CrearEgreso(CreateView):
    template_name = 'administrador/crud_egreso/crear.html'
    model = Egreso
    fields = ['anio', 'universidad', 'facultad', 'carrera', 'cantidad']
    success_url = reverse_lazy('info_app:egreso')

@login_required
def eliminar_egreso(request, pk):
    egreso = Egreso.objects.get(id=pk)
    egreso.delete()
    messages.success(request, 'El registro de egreso ha sido eliminada exitosamente.')
    return redirect('info_app:egreso')

@login_required
def egreso(request):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        universidad = request.POST.get('universidad')
        facultad = request.POST.get('facultad')
        carrera = request.POST.get('carrera')
        universidad = AsignarUniversidad(universidad)

        egresos = Egreso.objects.all()
        
        if((anio == "") and (universidad == "") and (facultad == "") and (carrera == "" )):
            egresos = Egreso.objects.all()
        elif((not anio == "") and (universidad == "") and (facultad == "") and (carrera == "" )):
            egresos = egresos.filter(anio=anio)
        elif((not anio == "") and (not universidad == "") and (facultad == "") and (carrera == "" )):
            egresos = egresos.filter(anio=anio, universidad=universidad)
        elif((not anio == "") and (not universidad == "") and (not facultad == "") and (carrera == "" )):
            egresos = egresos.filter(anio=anio, universidad=universidad, facultad=facultad)
        elif((not anio == "") and (not universidad == "") and (not facultad == "") and (not carrera == "" )):
            egresos = egresos.filter(anio=anio, universidad=universidad, facultad=facultad, carrera=carrera)

        datos = {
            'lista': egresos
        }
    else:
        datos = {
            'lista': Egreso.objects.all().order_by('universidad'),
            'titulo': 'Lista egresos',
        }
    return render(request, 'administrador/egreso.html', datos)

