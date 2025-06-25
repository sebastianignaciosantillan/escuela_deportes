from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from .decorators import administrador_required, supervisor_required, empleado_required
from .forms import EntrenadorForms

# Create your views here.
#entrada publica (landing page, home etc)
def index(request):
    return render(request, 'index.html',{
        
    })
    
# ****************  AUTH  ******************
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Redirige al dashboard segun el rol
            if user.is_administrador():
                return redirect('admin_dashboard')
            elif user.is_supervisor():
                return redirect('supervisor_dashboard')
            elif user.is_empleado():
                return redirect('empleado_dashboard')
            else:
                return redirect('acceso_denegado')  

        else:
            error = "Usuario o contraseña incorrectos."
            return render(request, 'auth/login.html', {'error': error})

    return render(request, 'auth/login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

# Cada tipo de usuario (rol) tendra su propio dashboard
@login_required
@administrador_required
def administrador_dashboard(request):
    return render(request, 'dashboards/administrador.html')

@login_required
@supervisor_required
def supervisor_dashboard(request):
    return render(request, 'dashboards/supervisor.html')

@login_required
@empleado_required
def empleado_dashboard(request):
    return render(request, 'dashboards/empleado.html')


@login_required
def redireccionar_dashboard(request):
    user = request.user
    if user.is_administrador():
        return redirect('admin_dashboard')
    elif user.is_supervisor():
        return redirect('supervisor_dashboard')
    elif user.is_empleado():
        return redirect('empleado_dashboard')
    else:
        # Redireccionar a alguna página de error o logout si no tiene rol válido
        return redirect('logout')  # o algún 403


#vista para error de acceso denegado

def acceso_denegado(request):
    return render(request, 'errors/acceso_denegado.html',{
        
    })    
    
