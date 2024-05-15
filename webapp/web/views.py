from flask import Flask, render_template
from users.controllers.user_controller import user_controller
from products.controllers.product_controller import product_controller
from users.models.db import db

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Registrando el blueprint del controlador de usuarios
app.register_blueprint(user_controller)
app.register_blueprint(product_controller)

# Ruta principal que lleva a menu.html
@app.route('/')
def index():
    return render_template('menu.html')

# Ruta para renderizar el template users.html
@app.route('/users/')
def users():
    return render_template('users.html')

# Ruta para renderizar el template products.html
@app.route('/products/')
def products():
    return render_template('products.html')

# Ruta para renderizar el template edit_users.html
@app.route('/edit_users/<string:id>')
def edit_user(id):
    print("id recibido",id)
    return render_template('edit_users.html', id=id)

# Ruta para renderizar el template edit_products.html
@app.route('/edit_products/<string:id>')
def edit_product(id):
    # Esta ruta se implementará cuando se cree el archivo edit_products.html
    print("id recibido",id)
    return render_template('edit_products.html', id=id)

if __name__ == '__main__':
    app.run()

