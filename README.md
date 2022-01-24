# library_api

_API básica de biblioteca con Django._

## Comenzando

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

_Antes de empezar es necesario asegurarse de tener un entorno con Python3, Sqlite3, Virtualenv, PIP y git, para poder realizar el proceso de instalación._

```
sudo apt-get install python3
sudo apt-get install sqlite3
sudo apt-get install python3-pip
sudo apt-get install virtualenv
sudo apt-get install python3-virtualenv
sudo apt-get install git
```

### Instalación 🔧

_Todas las instrucciones de consola a continuación están pensadas para ejecutarse en entornos con distribuciones Linux, pero cabe decir que pueden variar dependiendo de la distribución y también se pueden realizar de manera similar en entornos Windows y OS X:_

1. Clonar el repositorio del proyecto en el directorio de tu preferencia:

```
git clone https://github.com/jsolorzano/library_api.git
```

2. Preparar y activar un entorno virtual en la ubiciación que prefieras:

_Creación..._

```
python3 -m venv myvenv 
```

_Activación..._

```
source myvenv/bin/activate
```
_Donde 'myvenv' es el nombre de tu entorno virtual._
_Este paso es muy importante de realizar antes de pasar a los siguientes, ya que deberás tener activo tu virtualenv durante todo el proceso._
_Sabrás que tienes virtualenv iniciado cuando veas que la línea de comando en tu consola tiene el prefijo (myvenv)._


3. Actualizar pip:

_Antes de instalar Djando y demás dependencias del proyecto debes asegurarte de tener la última versión de pip, el software que usarás para instalar Django._

```
python -m pip install --upgrade pip
```

4. Instalar Django y demás dependencias:

_Para este proposito debes ubicarte en la raíz del proyecto clonado._

```
cd /ruta/proyecto/clonado
```

_Una vez ubicado debes ejecutar la instalación mediante el fichero de requisitos usando pip:_

```
pip install -r requirements.txt
```

5. Migrar modelos:

_Una vez instalados los paquetes en el paso 4, hay que realizar la migración de los modelos a la base de datos._
_Para este proposito también debes ubicarte en la raíz del proyecto clonado._

```
python manage.py migrate
```

6. Crear usuario superadmin:

```
python manage.py createsuperuser
```

_Cuando te lo pida, escribe tu nombre de usuario (en minúscula, sin espacios), email y contraseña._



## Ejecución 🚀

_Una vez realizados todos los pasos anteriores, ya estarás listo para ejecutar la aplicación._

```
python manage.py runserver
```
_Si haz llegado a este punto, tendrás a disposición el siguiente conjunto de endpoints para navegar la api._

_http://127.0.0.1:8000/api/v1/_

_http://127.0.0.1:8000/api/v1/auth/_

_http://127.0.0.1:8000/api/v1/auth/registration/_

_http://127.0.0.1:8000/authors/export_xlsx/_

_http://127.0.0.1:8000/books/export_xlsx/_

_En el primero de los endpoints encontrarás los enlaces a los endpoints de Autores y Libros y desde ellos podrás gestionar los modelos que cada uno representa._

_En el segundo y tercer endpoint son para logueo y registro de usuarios, generando un token de validación._

_Y los dos últimos son para exportar los datos que hayan sido registrados en los modelos de autores y libros._


---
⌨️ por [jsolorzano](https://gitlab.com/jsolorzano)
