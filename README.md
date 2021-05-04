# odoo

Backlog

Creación de módulo Informes GeoRedia (informe_geo)


Se crea una rama vacía con el README.md

Se crea un nuevo módulo, (o manualmente, o con uno de ejemplo o con scaffod, siendo esta última la más recomendable)

Se personaliza el __manifest__.py con el nombre, descripción, versión, autor, etc.

Se comienza creando el modelo

from odoo import models, fields, api

'''
class informe(models.Model):
    _name = 'informe_geo.informe'
    _description = 'Informe'

    name = fields.Char(string='Nombre')
    filename = fields.Char(string='Fichero')
    description = fields.Text(string='Descripción')
'''

Se sube para visualizar el modelo en modo debug, pero da un warning de que no se han añadido reglas de acces.

Se accede a la web y se comprueba que el módulo ha sido instalado (tras ponerlo en las instalaciones de inicio)

Se pone en modo debug y se accede al apartado "técnichal/models" y se aprecia que el modelo está correctamente cargado.

Creamos una vista de listado en el ficher views/views.xml  (a todos los ids se le intenta dar el nombre que comience por el nombre del módulo)



Damos permiso de acceso descomentando la línea de secirity en el __manifest__.py y actualizándola a:
'''
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_informe_geo_informe,informe_geo.informe,model_informe_geo_informe,base.group_user,1,1,1,1
'''


Añadimos datos de ejemplo al fichero demo/demo.xml que ya está referenciado desde el __manifest__.py


Creamos una vista formulario para que se pueda ver cada registro y crear

