from app import db

#tabla producto
class products (db.Model):
    __tablename__ = 'products'
    #agregar id uml
    id = db.Column (db.Integer, primary_key = True, autoincrement = True)    
    name = db.Column(db.String)
    codeProduct = db.Column(db.Integer)
    brand = db.Column(db.String, nullable=True)
    productType = db.Column(db.String, nullable=True)
    admissionDate = db.Column(db.Integer)
    measureUnit = db.Column(db.String)
    ivaTax = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    #salePrice = db.Column(db.Integer)

    def __init__(self, name, codeProduct, brand, productType, admissionDate, measureUnit, ivaTax, stock):
        self.name = name
        self.codeProduct = codeProduct
        self.brand = brand
        self.productType = productType
        self.admissionDate = admissionDate
        self.measureUnit = measureUnit
        self.ivaTax = ivaTax
        self.stock = stock
     #   self.salePrice = salePrice   

#tabla usuario
class user (db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    telephone = db.Column(db.String)
    role = db.Column(db.String)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    birthDate =db.Column(db.String)

#tabla ingreso
class Input (db.Model):
    __tablename__ = 'Input'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id_user = db.Column(db.ForeignKey("User.id"))
    codeProduct = db.Column(db.ForeignKey("products.codeProduct"))
    amount = db.Column(db.Integer)
    date = db.Column(db.ForeignKey("products.admissionDate"))
    purchasePrice = db.Column(db.Integer)
    percentageProfit = db.Column(db.Integer)    
#tabla detalle de venta
class Saledetail (db.Model):
    __tablename__ = 'Saledetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    idOutput = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    unitValue = db.Column(db.Integer)
    ivaTax = db.Column(db.Integer, unique = True)
    totalValue = db.Column(db.Integer, unique = True)  
'''#tabla salida
class Output (db.Model):
    __tablename__ = 'Output'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id_user = db.Column(db.ForeignKey("User.id"))
    purchasePrice = db.Column(db.ForeignKey("Input.purchasePrice"))
    idSaleDetail = db.Column(db.ForeignKey("Saledetail.id"))'''
