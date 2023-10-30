from django.shortcuts import render

def principal(request):
    titulo="The Geeks's House Store"
    context={
        "titulo":titulo
    }
    return render(request,"public/index.html",context)

def contacto(request):
    titulo="TGHS - Contacto"
    context={
        "titulo":titulo
    }
    return render(request,"public/contacto.html",context)