from flask import Flask, request
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

@app.route('/signup')
def signup_route():
    return 'REGISTER'

@app.route('/section')
def section():    
    return 'Section'
#ruta de otras acciones
@app.route('/product', methods=['GET','POST'])
def crud_product():
   if request.method == 'GET':
   #haga algo
    print("Arrived a GEt")
    #insertar porducto
    name = "Rice"
    codeProduct = 100
    brand = "Roa"
    productType = "Grains"
    admissionDate = 29092021
    measureUnit = "Kg"
    ivaTax = 19
    stock = 5
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
   