# T-MOB Ejercicio(Python/Django)

[![Alt text](https://img.youtube.com/vi/0_dBzI441Ck/0.jpg)](https://www.youtube.com/watch?v=0_dBzI441Ck)


## :hammer_and_wrench: Descarga y puesta a punto del proyecto (windows):

- Desde la terminal realizar un clone del proyecto( ejecutar un git clone https://github.com/rodri-valladares/t-mob-python.git )
- Crear entorno `python -m venv env`
- Dentro de la carpeta del entorno creado, activar entorno( `.\env\Scripts>activate`)
- Ya con el entorno activo dirigirse a la carpeta descargada/clonada, acceder a la carpeta ejercicio e instalara los paquetes: `pip install -r requirements.txt`
- Crear base de datos. Para la prueba en local se definió una base de datos con los siguientes datos: `'NAME': 'test_local',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '3306' `
- Realizar y ejecutar migraciones(base de datos) : `python manage.py makemigrations` posteriormente ejecutar `python manage.py migrate`
- Crear superuser : `python manage.py createsuperuser` (se le solicitara elegir un user y un pass)

## Instalaciones necesarias:
Al ejecutar el proyecto en local debe estar tambien ejecutando memcached. Para instalar memcached puede dirigirse a: https://www.apachelounge.com/viewtopic.php?t=7919 . El proyecto fue probado con la version 1.6.0 ( https://github.com/nono303/memcached/tree/1.6.0 ) 

Esta configurado para funcionar con MYSQL, puede descargarlo: https://dev.mysql.com/downloads/windows/installer/8.0.html 

## :rocket: Ejecutar aplicación:
- Ejecutar memcached: Dirigirse a la carpeta descargada desde terminal y ejecutar: `memcached.exe -m 512 -vvv`
- Desde otra terminal acceder al proyecto descargado, a la altura del manage.py ejecutar `python manage.py runserver`
- Ingresar desde cualquier navegador a la ruta local sugerida. Por lo general: http://127.0.0.1:8000/

## Como usar:
Se pueden crear registros desde el admin: http://localhost:8000/admin/
En caso que se guarde un registro con active en True este se guardará en cache

Se puede listar todos los registros en formato JSON : http://localhost:8000/key-list/

Se puede pasar una key y se retornará un JSON con la key y la URL: http://localhost:8000/key-list/<key_previamente_creada>/
En caso que la key ingresada se encuentre en cache la obtendrá de esta.

