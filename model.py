import web

db_host = 'localhost'
db_name = 'productos' 
db_user = 'root'
db_pw   = ''

db = web.database(
			dbn='mysql',
			host=db_host,
			db=db_name,
			user=db_user,
			pw=db_pw
			)

def get_productos():
	try:
		return db.select('productos')
	except:
		return None

def get_producto(id_producto):
	try:
		return db.select('productos',where ='id_productos=$id_producto',vars = locals())
	except:
		return None 