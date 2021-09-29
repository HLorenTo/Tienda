from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/mitiendadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)
#Importar modelos
from models import products


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

@app.route('/createuser', methods=['POST'])
def create_user():
    email = request.form["email"]
    password = request.form["password"]
    user = User(email, password)  
    db.session.add(user)  
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
@app.route('/product', methods=['GET','POST'])
def crud_product():
   if request.method == 'GET':
   #haga algo
    print("Arrived a GEt")
    #insertar porducto
    name = "Milk"
    codeProduct = 101
    brand = "Colanta"
    productType = "Lacteos"
    admissionDate = 30092021
    measureUnit = "ml"
    ivaTax = 19
    stock = 10
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
       #salePrice = request_data['saleprice'] 
       print("Name:" + name)
       print ("Code product: "+ codeproduct)
       print ("Brand product: "+ brand)
       print ("Type product: "+ productType)
       print ("Admission date product: "+ admissionDate)
       print ("Measure unit product: "+ measureUnit)
       print ("Iva Tax: "+ ivaTax)
       print ("Stock product: "+ stock)
       #print ("Sale price product: "+ salePrice)
       return 'Registered product'
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
