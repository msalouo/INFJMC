from django.shortcuts import render

def home(request):
    return render(request, 'CORE/home.html') 

def carreras(request):
    lista_carreras = ['Ingeniería en Sistemas Computacionales', 'Ingeniería Industrial', 
                      'Ingeniería Mecatrónica', 'Ingeniería en Energías Renovables', 
                      'Ingeniería en Gestión Empresarial', 'Ingeniería en Logística y Transporte', 
                      'Ingeniería en Tecnologías de la Información y Comunicación']
    
    return render(request, 'CORE/carreras.html', {'carreras': lista_carreras})

def docentes(request):
    lista_docentes = ['Dr. Juan Pérez', 'Dra. María López', 'Ing. Carlos Sánchez', 
                      'Lic. Ana Torres', 'Mtro. Luis Ramírez', 'Dra. Laura Gómez', 
                      'Ing. Pedro Martínez']
    
    return render(request, 'CORE/docentes.html', {'docentes': lista_docentes})

# Create your views here.
