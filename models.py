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
#tabla inventario
class inventary (db.Model):
    __tablename__ = 'inventary'
    #agregar id uml
    id = db.Column (db.Integer, primary_key = True, autoincrement = True)    
    name = db.Column(db.ForeignKey("products.name"))
    codeProduct = db.Column(db.ForeignKey("products.codeProduct"))
    brand = db.Column(db.ForeignKey("products.brand"))
    productType = db.Column(db.ForeignKey("products.productType"))
    admissionDate = db.Column(db.ForeignKey("products.admissionDate"))
    measureUnit = db.Column(db.ForeignKey("products.measureUnit"))
    ivaTax = db.Column(db.ForeignKey("products.ivaTax"))
    stock = db.Column(db.ForeignKey("products.stock"))
    amount = db.Column(db.ForeignKey("Input.amount"))
    def __init__(self, name, codeProduct, brand, productType, admissionDate, measureUnit, ivaTax, stock, amount):
        self.name = name
        self.codeProduct = codeProduct
        self.brand = brand
        self.productType = productType
        self.admissionDate = admissionDate
        self.measureUnit = measureUnit
        self.ivaTax = ivaTax
        self.stock = stock
        self.amount = amount
#tabla usuario
class newuser (db.Model):
    __tablename__ = 'NewUser'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    telephone = db.Column(db.String)
    role = db.Column(db.String)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    birthDate =db.Column(db.String)
    def __init__(self, email, password, telephone, role, name, lastname, birthDate):
        self.email = email
        self.password = password
        self.telephone = telephone
        self.role = role
        self.name = name
        self.lastname = lastname
        self.birthDate = birthDate
#Tabla user
class user (db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
#tabla ingreso
class Input (db.Model):
    __tablename__ = 'Input'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id_user = db.Column(db.ForeignKey("NewUser.id"))
    codeProduct = db.Column(db.ForeignKey("products.codeProduct"))
    amount = db.Column(db.Integer)
    date = db.Column(db.ForeignKey("products.admissionDate"))
    purchasePrice = db.Column(db.Integer)
    percentageProfit = db.Column(db.Integer)    
    def __init__(self, id_user, codeProduct, amount, date, purchasePrice, percentageProfit):
        self.id_user = id_user
        self.codeProduct = codeProduct
        self.amount = amount
        self.date = date
        self.purchasePrice = purchasePrice
        self.percentageProfit = percentageProfit
#tabla detalle de venta
class Saledetail (db.Model):
    __tablename__ = 'Saledetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    idOutput = db.Column(db.Integer)
    amount = db.Column(db.ForeignKey("Input.amount"))
    unitValue = db.Column(db.Integer)
    ivaTax = db.Column(db.Integer, unique = True)
    totalValue = db.Column(db.Integer, unique = True)  
    def __init__(self, idOutput, amount, unitValue, ivaTax,totalValue):
        self.idOutput = idOutput
        self.amount = amount
        self.unitValue = unitValue
        self.ivaTax = ivaTax
        self.totalValue = totalValue
'''#tabla salida
class Output (db.Model):
    __tablename__ = 'Output'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id_user = db.Column(db.ForeignKey("User.id"))
    purchasePrice = db.Column(db.ForeignKey("Input.purchasePrice"))
    idSaleDetail = db.Column(db.ForeignKey("Saledetail.id"))'''
