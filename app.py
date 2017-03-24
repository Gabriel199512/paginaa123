import web
import model  
urls = (
    '/index', 'Index',
   '/modificar', 'Modificar',
   '/delete', 'Delete',
    '/ver/(.+)', 'Ver',
)
app = web.application(urls, globals())
render= web.template.render('templates', base = 'master') 

web.config.debug = False

class Modificar:        
    def GET(self):		
		return render.modificar()

class Borrar:        
    def GET(self):		
		return render.borrar()

class Ver:
    def GET(self, id):
    	id_producto = int(id)
    	producto = model.get_producto(id_producto)
    	return render.ver(producto)

class Index:        
    def GET(self):
    	productos = model.get_productos()		
        return render.index(productos)

if __name__ == "__main__":
    app.run()