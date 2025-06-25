
pasos:
clonar el repositorio con git clone <nombre_del_repositorio_aqui>
abrir el proyecto y crear un entorno virtual (recomendado para no instalar las dependencias a nivel global)
abrir el proyecto con visual estudio code
abrir la consola y escribir pip install -r requirements.txt para instalar las dependencias de este proyecto

corre:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   (cargar los datos como nombre, correo y contraseña)

(deje comentado estas líneas para simplificar el correr el proyecto )
# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

pero deben crear un archivo llamado .env en la raíz del proyecto y cargar la información de:

# Seguridad
SECRET_KEY= <tu clave segura de ejemplo que te da django y esta en settings>
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

tras hacer eso pueden correr
python manage.py runserver

cualquier duda me escriben a mi cel 3855057114 mucha suerte futuros colegas a