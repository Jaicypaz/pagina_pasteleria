from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'texto': 'Índice'}) #recuerda que lleva tilde debe estar asi en las otras carpetas

def about(request):
    return render(request, 'about.html', {'texto': 'Acerca'})

def welcome(request):
    return render(request, 'welcome.html', {'texto': 'Bienvenido cliente'})

#seccion llamada indice 