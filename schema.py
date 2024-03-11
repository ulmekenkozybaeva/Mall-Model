from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./todo.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Pydantic models

class BrandCreate(BaseModel):
    brandname = str
    description = str


class Brand(BrandCreate):
    id = int


class CategorieCreate(BaseModel):
    categoriename = str
    description = str


class Categorie(CategorieCreate):
    id = int


class MaterialCreate(BaseModel):
    materialname = str
    description = str


class Material(MaterialCreate):
    id = int


class ProductinfoCreate(BaseModel):
    productname = str
    description = str
    brand_id = int
    material_id = int
    categories_id = int


class Productinfo(ProductinfoCreate):
    id = int


class MallCreate(BaseModel):
    mallname = str
    address = str


class Mall(MallCreate):
    id = int


class ProductsCreate(BaseModel):
    products_id = int
    count = int
    mall_id = int


class Products(ProductsCreate):
    id: int


class BasketCreate(BaseModel):
    products_id = int
    count = int


class Basket(BasketCreate):
    id: int


class StaffCreate(BaseModel):
    firstname = str
    lastname = str


class Staff(StaffCreate):
    id: int


class CourierCreate(BaseModel):
    firstname = str
    lastname = str


class Courier(CourierCreate):
    id = int


class CustomerCreate(BaseModel):
    firstname = str
    lastname = str


class Customer(CustomerCreate):
    id: int


class CustomerHasBasketCreate(BaseModel):
    products_id = int
    customer_id = int


class CustomerHasBasket(CustomerHasBasketCreate):
    id = int


class OrderCreate(BaseModel):
    customerhasbasket_id = int
    staff_id = int
    courier_id = int
    createAt = int
    overall = int


class Order(OrderCreate):
    id = int


# Database Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
