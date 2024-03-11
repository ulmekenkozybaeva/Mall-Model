from fastapi import FastAPI
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
import model
import schema

# FastAPI Setup
app = FastAPI()
# Basket Routes

@app.post("/baskets/", response_model=model.Basket)
def create_basket(basket: BasketCreate, db: Session = Depends(schema.get_db)):
    new_basket = model.Basket(**basket.dict())
    db.add(new_basket)
    db.commit()
    db.refresh(new_basket)
    return new_basket

@app.get("/baskets/{basket_id}", response_model=model.Products)
def read_basket(basket_id: int, db: Session = Depends(schema.get_db)):
    basket = db.query(model.Basket).filter(model.Basket.id == basket_id).first()
    if not basket:
        raise HTTPException(status_code=404, detail="Basket not found")
    return basket

@app.get("/baskets/", response_model=list[model.Basket])
def read_baskets(skip: int = 0, limit: int = 10, db: Session = Depends(schema.get_db)):
    baskets = db.query(model.Basket).offset(skip).limit(limit).all()
    return baskets

@app.delete("/baskets/{basket_id}", response_model=model.Basket)
def delete_basket(basket_id: int, db: Session = Depends(schema.get_db)):
    basket = db.query(model.Basket).filter(model.Basket.id == basket_id).first()
    if not basket:
        raise HTTPException(status_code=404, detail="Basket not found")
    db.delete(basket)
    db.commit()
    return basket

# Staff Routes
@app.post("/staffs/", response_model=model.Staff)
def create_staff(staff: schema.StaffCreate, db: Session = Depends(schema.get_db)):
    new_staff = model.Staff(**staff.dict())
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

@app.get("/staffs/{staff_id}", response_model=model.Staff)
def read_staff(staff_id: int, db: Session = Depends(schema.get_db)):
    staff = db.query(model.Staff).filter(model.Staff.id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff

@app.get("/staffs/", response_model=list[model.Staff])
def read_staffs(skip: int = 0, limit: int = 10, db: Session = Depends(schema.get_db)):
    staffs = db.query(model.Staff).offset(skip).limit(limit).all()
    return staffs

@app.delete("/staffs/{staff_id}", response_model=model.Staff)
def delete_staff(staff_id: int, db: Session = Depends(schema.get_db)):
    staff = db.query(model.Staff).filter(model.Staff.id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    db.delete(staff)
    db.commit()
    return staff

# Courier Routes
@app.post("/courier/", response_model=model.Courier)
def create_courier(courier: schema.CourierCreate, db: Session = Depends(schema.get_db)):
    new_courier = model.Courier(**courier.dict())
    db.add(new_courier)
    db.commit()
    db.refresh(new_courier)
    return new_courier

@app.get("/courier/{courier_id}", response_model=model.Courier)
def read_courier(courier_id: int, db: Session = Depends(schema.get_db)):
    courier = db.query(model.Courier).filter(model.Courier.id == courier_id).first()
    if not courier:
        raise HTTPException(status_code=404, detail="Courier not found")
    return courier

@app.get("/courier/", response_model=list[model.Courier])
def read_Courier(skip: int = 0, limit: int = 10, db: Session = Depends(schema.get_db)):
    couriers = db.query(model.Courier).offset(skip).limit(limit).all()
    return couriers

@app.delete("/courier/{courier_id}", response_model=model.Courier)
def delete_Courier(courier_id: int, db: Session = Depends(schema.get_db)):
    courier = db.query(model.Courier).filter(model.Courier.id == courier_id).first()
    if not courier:
        raise HTTPException(status_code=404, detail="Courier not found")
    db.delete(courier)
    db.commit()
    return courier

# Customer Routes
@app.post("/customers/", response_model=model.Customer)
def create_customer(customer: schema.CustomerCreate, db: Session = Depends(schema.get_db)):
    new_customer = model.Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@app.get("/customers/{customer_id}", response_model=model.Customer)
def read_customer(customer_id: int, db: Session = Depends(schema.get_db)):
    customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.get("/customers/", response_model=list[model.Customer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(schema.get_db)):
    customers = db.query(model.Customer).offset(skip).limit(limit).all()
    return customers

@app.delete("/customers/{customer_id}", response_model=model.Customer)
def delete_customer(customer_id: int, db: Session = Depends(schema.get_db)):
    customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return customer

# CustomerHasBasket Routes
@app.post("/customerHasBasket/", response_model=model.CustomerHasBasket)
def create_customerhasbasket(customerHasBasket: schema.CustomerHasBasketCreate, db: Session = Depends(schema.get_db)):
    new_customerHasBasket = model.CustomerHasBasket(**customerHasBasket.dict())
    db.add(new_customerHasBasket)
    db.commit()
    db.refresh(new_customerHasBasket)
    return new_customerHasBasket

@app.get("/customerHasBasket/{customerHasBasket_id}", response_model=model.CustomerHasBasket)
def read_customerhasbasket(customerHasBasket_id: int, db: Session = Depends(schema.get_db)):
    customerHasBasket = db.query(model.CustomerHasBasket).filter(model.CustomerHasBasket.id == customerHasBasket_id).first()
    if not customerHasBasket:
        raise HTTPException(status_code=404, detail="CustomerHasBasket not found")
    return customerHasBasket

@app.get("/customerHasBasket/", response_model=list[model.CustomerHasBasket])
def read_customerHasBaskets(skip: int = 0, limit: int = 10, db: Session = Depends(schema.get_db)):
    customerHasBaskets = db.query(model.CustomerHasBasket).offset(skip).limit(limit).all()
    return customerHasBaskets

@app.delete("/customerHasBasket/{customerHasBasket_id}", response_model=model.CustomerHasBasket)
def delete_customerHasBasket(products_id: int, db: Session = Depends(schema.get_db)):
    customerHasBasket = db.query(model.CustomerHasBasket).filter(model.CustomerHasBasket.id == products_id).first()
    if not customerHasBasket:
        raise HTTPException(status_code=404, detail="CustomerHasBasket not found")
    db.delete(customerHasBasket)
    db.commit()
    return customerHasBasket

# Order Routes
@app.post("/orders/", response_model=model.Order)
def create_order(order: schema.OrderCreate, db: Session = Depends(schema.get_db)):
    new_order = model.Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@app.get("/orders/{order_id}", response_model=model.Order)
def read_order(order_id: int, db: Session = Depends(schema.get_db)):
    order = db.query(model.Order).filter(model.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/orders/", response_model=list[model.Order])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(schema.get_db)):
    orders = db.query(model.Order).offset(skip).limit(limit).all()
    return orders

@app.delete("/orders/{order_id}", response_model=model.Order)
def delete_order(order_id: int, db: Session = Depends(schema.get_db)):
    order = db.query(model.Order).filter(model.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return order