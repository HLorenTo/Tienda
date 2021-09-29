from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/mitiendadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'
db = SQLAlchemy(app)
#Importar modelos
from models import products, NewUser, products
#crear el esquema de la db
db.create_all()
db.session.commit()
#rutas de paginas
@app.route('/home')
def home_route():
    return 'This is the home'
@app.route('/register')
def register():
    return render_template("register.html")
@app.route('/create-user', methods=['POST'])
def create_user():
    email = request.form["email"]
    password = request.form["password"]
    telephone = request.form["telephone"]
    role = request.form["role"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    birthDate = request.form["birthDate"]
    newUser = NewUser(email, password, telephone, role, name, lastname, birthDate)  
    db.session.add(newUser)  
    db.session.commit()
    return "ok"

@app.route('/section')
def section():    
    return render_template("section.html")
@app.route('/inventary', methods=['POST'])    
def inventary():
    code_product = request.form["code_product"]
    print ("The code product is: ")
    print(code_product)
    #return "Inventary"
    return render_template("inventary.html")

@app.route('/store', methods=['POST'])    
def store():
    code_user = request.form["code_user"]
    print ("The code user is: ")
    print(code_user)
    return "Store"    
#ruta de otras acciones
'''@app.route('/product', methods=['GET','POST'])
def crud_product():
   if request.method == 'GET':
   #haga algo
    print("Arrived a GEt")
    #insertar porducto
    name = "Milk"
    codeProduct = 101
    brand = "Colantasssss"
    productType = "Lacteos"
    admissionDate = 30092021
    measureUnit = "ml"
    ivaTax = 19
    stock = 10
#    stockmin = 10
#    amount = 30
    entry = products(name, codeProduct, brand, productType, admissionDate, measureUnit, ivaTax, stock)
    db.session.add(entry)
    db.session.commit()
    return 'This was a get'
   elif request.method == 'POST':
       #registrar producto
       request_data = request.form
       name = request_data['name']
       codeproduct = request_data['codeproduct']   
       brand = request_data['brand']   
       productType = request_data['productType']   
       admissionDate = request_data['admissionDate']   
       measureUnit = request_data['measureUnit']   
       ivaTax = request_data['ivaTax']   
       stock = request_data['stock']   
       #stockmin = request_data['stockmin']   
       #amount = request_data['amount']   
       Products = products(name, codeproduct, brand, productType, admissionDate, measureUnit, ivaTax, stock)  
       db.session.add(Products)  
       db.session.commit()
       return "ok"'''
#insertar producto html
@app.route('/newproducts')
def newproducts():
    return render_template("newproducts.html")
@app.route('/create-p', methods=['POST'])
def create_product():
        name = request.form["name"]
        codeproduct = request.form['codeproduct']   
        brand = request.form['brand']   
        productType = request.form['productType']   
        admissionDate = request.form['admissionDate']   
        measureUnit = request.form['measureUnit']   
        ivaTax = request.form['ivaTax']   
        stock = request.form['stock'] 
       # stockmin = request.form['stockmin'] 
      #  amount = request.form['amount'] 
        Products = products(name, codeproduct, brand, productType, admissionDate, measureUnit, ivaTax, stock)  
        db.session.add(Products)  
        db.session.commit()
        return "ok"









#Actualizar producto
@app.route ('/updateproduct')
def update_product():
    old_name = "Rice"
    new_name = "Beans"
    old_product = products.query.filter_by(name=old_name).first()        
    old_product.name = new_name
    db.session.commit()
    return "Updated sucessfully"
#traer productos
@app.route ('/getproduct')
def get_product():
    product = products.query.all()
    print(product[0].name)
    return "This are the products"

#borrar producto
@app.route ('/deleteproduct')    
def delete_song():
    product_name = "Milk"
    product = products.query.filter_by(name=product_name).first()
    db.session.delete(product)
    db.session.commit()
    return "Deleted porduct"
