from flask import Flask, request
app = Flask(__name__)

@app.route('/home')
def home_route():
    return 'This is the home'

@app.route('/signup')
def signup_route():
    return 'REGISTER'

@app.route('/section')
def section():    
    return 'Section'

@app.route('/product', methods=['GET','POST'])
def crud_product():
   if request.method == 'GET':
   #haga algo
    print("Arrived a GEt")
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
   