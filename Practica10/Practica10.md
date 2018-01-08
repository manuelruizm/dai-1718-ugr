# Práctica 10

En esta práctica hay que realizar el despliegue de una aplicación web para que funcione como lo haría una vez que estuviera lista, sin modo de depuración y lista para servir contenidos.

En mi caso he utilizado como aplicación una copia de la aplicación de las prácticas 6 a 9. Para ello he copiado todo el contenido de estas prácticas en un directorio llamado Practica10. Como se trabajó en esas prácticas, el ambiente de desarrollo está activo y lo primero que hay que hacer es deshabilitarlo y pasar a un ambiente de producción. Para ello, en el archivo settings.py de la aplicación principal hay que cambiar dos líneas de código y poner lo que aparece a continuación:

```python
DEBUG = False
ALLOWED_HOSTS = [‘*’]
```

Ahora voy a instalar en la máquina virtual una serie de servicios que permitirán lanzar esta aplicación en el ambiente de producción simulado que estamos creando.

1. **Gunicorn**, un servidor web WSGI que sustituye al runserver de desarrollo.

	```bash
	sudo pip3 install gunicorn
	```

2. **Nginx**, un servidor web/proxy inverso con balanceo de carga, servidor de archivos estáticos, etc. Será el encargado de servir los archivos en /static una vez abandonado el ambiente de desarrollo ya que Django no se encargará de servirlos en ese caso.

	```bash
	sudo apt-get install nginx
	```

3. **Supervisord**, un servicio utilizado para arrancar y mantener arrancado un servidor web como gunicorn. Será el encargado de que dicho proceso esté siempre en ejecución.

	```bash
	sudo apt-get install supervisord
	```

Una vez que estos tres servicios están instalados en nuestra máquina virtual podemos realizar la configuración de los mismos, y de la máquina virtual, para que se pueda servir la aplicación web en el ambiente de producción.

En primer lugar, hay que saber cómo están configurados los puertos de la máquina virtual para conocer a través de qué puertos se realiza la petición al servidor.

	config.vm.network "forwarded_port", guest: 80, host: 80

Para que funcione normalmente hay que configurar Vagrantfile para que la máquina virtual escuche las solicitudes por el puerto 80, para que a la hora de solicitar el recurso a través de la URL no haya que indicar el puerto.

En segundo lugar, para comprobar que gunicorn efectivamente está funcionando se ejecuta el comando:

	sudo /usr/local/bin/gunicorn Practica10.wsgi -b:80

Esto permitirá que todas las solicitudes que lleguen a la máquina virtual por el puerto 80 sean escuchadas y servidas por gunicorn.

Así, solicitando el recurso a través de “localhost”, gunicorn ya nos mostrará el contenido de la aplicación web, pero sin cargar los archivos estáticos ya que aún no se ha configurado nginx.

Antes de configurar nginx vamos hacer uso de supervisord, ya que si cada vez que queremos tener el servidor activo vamos a tener que ejecutar la orden anterior de gunicorn no estamos avanzando nada. Por ello, gracias a supervisord podemos hacer que gunicorn se quede funcionando en segundo plano para siempre. Esto lo vamos a conseguir modificando el archivo /etc/supervisord/supervisord.conf. Para ello ejecutamos la orden

	sudo nano /etc/supervisord/supervisord.conf

y escribimos justo al final del archivo las siguientes líneas:

```code
[program:gunicorn]
command=sudo /usr/local/bin/gunicorn Practica10.wsgi -b:80
directory=/home/manolo/Proyectos/Practica10/restaurantes/
user=vagrant
autostart=true
autorestart=true
redirect_stderr=true
```

Reiniciando el servicio, de nuevo podemos acceder a través de “localhost” y ver los mismos resultados de antes, pero esta vez de forma continua ya que gunicorn estará continuamente activo.

Finalmente, vamos a configurar nginx y la aplicación para que se pueda servir el contenido estático.

En el archivo settings.py de la aplicación hay que añadir el directorio desde el que se va a servir el contenido estático que para que nginx lo sirva será en /var/www/static. Por ello hay que añadir la siguiente línea:

```code
STATIC_ROOT=’/var/www/static’
```

Además, hay que copiar el contenido estático en esa ruta, por lo que se ejecuta también el siguiente comando estando sobre la ruta en la que se encuentra static:

	cp -r static/ /var/www/static

Ahora paso a configurar nginx. Para ello hay que crear un archivo de configuración, utilizando el siguiente comando (con el editor nano por ejemplo):

	sudo nano /etc/nginx/sites-available/Practica10

En dicho archivo hay que incluir las siguientes líneas:

```code
server {
     listen 80 default_server;

     # servidor web para archivos en  /static
     location /static/ {
                alias /var/www/static/;
     }

     # proxy inverso, se pasa a la aplicación wsgi
     location / {
           proxy_pass http://127.0.0.1:8080;
           proxy_set_header X-Forwarded-Host $server_name;
           proxy_set_header X-Real-IP $remote_addr;
     }
}
```

Con esto, nginx escuchará lo que se solicité por el puerto 80 y devolverá lo que encuentre en el puerto indicado por el proxy inverso, en este caso el 8080. Si recordamos, nosotros habíamos configurado gunicorn y supervisord para que la aplicación se sirviera en el puerto 80. Simplemente tenemos que cambiar esto para que ahora se sirva la aplicación web en el 8080 que es donde va a buscar nginx y además ya sabe donde buscar el contenido estático, por lo que se devolverá la aplicación completa.

Por último hay que crear un enlace simbólico del archivo de configuración que se ha creado para nginx:

	sudo ln -s /etc/nginx/sites-enabled /etc/nginx/sites-available/Practica10

Reiniciando los servicios, ya está listo todo para que se pueda servir todo el contenido perfectamente en el ambiente de producción.

	sudo service supervisord restart
	sudo service nginx restart

Accediendo a través de “localhost” podemos comprobar que el contenido se muestra a la perfección.
