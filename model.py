
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

DATABASE_URL = "sqlite:///./todo.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Brand(Base):
    __tablename__ = "Brand"

    id = Column(Integer, primary_key=True, index=True)
    brandname = Column(String, index=True)
    description = Column(String, index=True)
    Productinfo = relationship("Productinfo")

class Categorie(Base):
    __tablename__ = "Categorie"

    id = Column(Integer, primary_key=True, index=True)
    categoriename = Column(String, index=True)
    description = Column(String, index=True)
    Productinfo = relationship("Productinfo")

class Material(Base):
    __tablename__ = "Material"

    id = Column(Integer, primary_key=True, index=True)
    materialname = Column(String, index=True)
    description = Column(String, index=True)
    Productinfo = relationship("Productinfo")

class Productinfo(Base):
    __tablename__ = "Productinfo"

    id = Column(Integer, primary_key=True, index=True)
    productname_id = Column(String, index=True)
    description_id = Column(String, index=True)
    brand_id = Column(Integer, ForeignKey('Brand.id'))
    material = Column(Integer, ForeignKey('Material.id'))
    categories = Column(Integer, ForeignKey('Categorie.id'))
    Products = relationship("Products")

class Mall(Base):
    __tablename__ = "Mall"

    id = Column(Integer, primary_key=True, index=True)
    mallname = Column(String, index=True)
    address = Column(String, index=True)
    Products = relationship("Products")
    Order = relationship("Order")

class Products(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, index=True)
    products_id = Column(Integer, ForeignKey('Productinfo.id'))
    count = Column(Integer, index=True)
    mall_id = Column(Integer, ForeignKey('Mall.id'))
    Basket = relationship("Basket")

class Basket(Base):
    __tablename__ = "Basket"

    id = Column(Integer, primary_key=True, index=True)
    products_id = Column(Integer, ForeignKey('Products.id'))
    count = Column(Integer, index=True)
    CustomerHasBasket = relationship("CustomerHasBasket")

class Staff(Base):
    __tablename__ = "Staff"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    Order = relationship("Order")

class Courier(Base):
    __tablename__ = "Courier"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    Order = relationship("Order")

class Customer(Base):
    __tablename__ = "Customer"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    CustomerHasBasket = relationship("CustomerHasBasket")
    Order = relationship("Order")

class CustomerHasBasket(Base):
    __tablename__ = "CustomerHasBasket"

    id = Column(Integer, primary_key=True, index=True)
    products_id = Column(Integer, ForeignKey('Basket.id'))
    customer_id = Column(Integer, ForeignKey('Customer.id'))
    Order = relationship("Order")

class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, index=True)
    customerhasbasket_id = Column(Integer, ForeignKey('CustomerHasBasket.id'))
    staff_id = Column(Integer, ForeignKey('Staff.id'))
    courier_id = Column(Integer, ForeignKey('Courier.id'))
    createAt = Column(Integer, index=True)
    overall = Column(Integer, index=True)

Base.metadata.create_all(bind=engine)