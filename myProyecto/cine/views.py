from django.shortcuts import render
from .models import Categoria,Pelicula #importar el modelo
#para lograr el ingreso de usuarios registrados al sistema,se debe 
#incorporar el modelo de usuarios registrados de Django
from django.contrib.auth.models import User #Auth autenticacion
# importar el sistema de autentificacion 
from django.contrib.auth import authenticate,logout,login as auth_login
#importar los "decorators" que permiten evitar el ingreso a una pagina
#sin estar logeado
from django.contrib.auth.decorators import login_required
# Create your views here. crear los controladores
# para las paginas web
@login_required(login_url='/login/')
def home(request):
    return render(request,'core/home.html')
    # retorna la pagina renderizada
def login(request):
    return render(request,'core/login.html')
def login_iniciar(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        p=request.POST.get("txtPass")
        usu=authenticate(request,username=u,password=p)
        if usu is not None and usu.is_active:
            auth_login(request, usu)
            return render(request,'core/home.html')
    return render(request,'core/login.html')
    
@login_required(login_url='/login/')
def eliminar_pelicula(request,id):#Metodos
    mensaje=''
    peli=Pelicula.objects.get(name=id)
    try:
        peli.delete()
        mensaje='Eliminó pelicula'
    except:
        mensaje='No pudo eliminar pelicula'

    pelis=Pelicula.objects.all()
    return render(request,'core/galeria.html',{'listapelis':pelis,'msg':mensaje})
@login_required(login_url='/login/')
def galeria(request):
    pelis=Pelicula.objects.all()#select * from pelicula
    return render(request, 'core/galeria.html',{'listapelis':pelis})
@login_required(login_url='/login/')
def quienes_somos(request):
    return render(request,'core/quienes_somos.html')
@login_required(login_url='/login/')
def formulario2(request):
    cate=Categoria.objects.all()# select * from Categoria
    if request.POST: 
        titulo=request.POST.get("txtTitulo")
        precio=request.POST.get("txtPrecio")
        duracion=request.POST.get("txtDuracion")
        descripcion=request.POST.get("txtDescripcion")
        categoria=request.POST.get("cboCategoria")
        #especie de select con un where incluido
        #recupera el objeto con 'name' enviado desde el comboBox (cboCategoria)
        obj_categoria=Categoria.objects.get(name=categoria) #se pone Categoria en mayuscula por hacer alucion al modelo
        #recuperar imagen desde el formulario
        imagen=request.FILES.get("txtImagen")
        #crear una instancia de Pelicula(modelo)
        pelicula=Pelicula(
            name=titulo,
            duracion=duracion,
            precio=precio,
            descripcion=descripcion,
            categoria=obj_categoria, #se hace alucion al objeto,las tablas se manejan por objetos
            imagen=imagen
        )
        pelicula.save() #graba el objeto instancial en bdd
        return render(request,'core/formulario2.html',{'lista':cate,'msg':'grabo','sw':True})#se muestra el mensaje de grabó,y con el true se activa
    return render(request,'core/formulario2.html',{'lista':cate}) #pasan los datos a la web
@login_required(login_url='/login/')
def formulario(request):
    mensaje=''
    sw=False
    if request.POST:
        accion=request.POST.get("Accion")
        if accion=="Grabar":
            name=request.POST.get("txtCate")
            cali=request.POST.get("txtCalificacion")
            CATE=Categoria(
                name=name,
                calificacion=cali
            )
            CATE.save()
            mensaje='Grabo'    
            sw=True
        if accion=="Eliminar":
            name=request.POST.get("txtCate")
            cate=Categoria.objects.get(name=name)
            cate.delete()
            mensaje='Elimino'
            sw=True

    categorias=Categoria.objects.all()# select * from categoria
    return render(request,'core/formulario.html',{'lista':categorias,'msg':mensaje,'sw':True})