from django.http import HttpResponse

def tercera_vista(request):
    return HttpResponse("<h1>Bienvenido a la Tercera Vista</h1><p>Esta es una espectacular tienda de deportes para árboles, para que tu árbol crezca como el actor que interpreta a terminator.</p>")

def cuarta_vista(request):
    return HttpResponse("<h1>Cuarta Vista</h1><p>Esta es una tienda de dinosaurios, puedes comprar y vender los tuyos!</p>")