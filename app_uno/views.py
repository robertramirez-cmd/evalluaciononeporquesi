from django.http import HttpResponse

def primera_vista(request):
    return HttpResponse("<h1>Bienvenido a la Primera Vista</h1><p>Esta es una tienda de ventas, donde compras para que vendan productos.</p>")

def segunda_vista(request):
    return HttpResponse("<h1>Segunda Vista</h1><p>Hola, esta es una vista,. aquí están los nuevos juegos del momento.</p>")