from django.shortcuts import redirect
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')

            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return redirect('acceso_denegado') 
        return _wrapped_view
    return decorator

def administrador_required(view_func):
    return role_required(['administrador'])(view_func)

def supervisor_required(view_func):
    return role_required(['supervisor'])(view_func)

def empleado_required(view_func):
    return role_required(['empleado'])(view_func)
