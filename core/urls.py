from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    #AUTH
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboards por rol
    path('dashboard/', views.redireccionar_dashboard, name='dashboard'),

    path('administrador/dashboard/', views.administrador_dashboard, name='admin_dashboard'),
    path('supervisor/dashboard/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('empleado/dashboard/', views.empleado_dashboard, name='empleado_dashboard'),
    
    path('acceso-denegado/', views.acceso_denegado, name='acceso_denegado'),


]
