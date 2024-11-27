from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List


DATA_BASE_NAME = "api_database"
USER = "api"
# Not recommended i will Process this later
PASSWORD = os.getenv('PASSWORD', 'default_version')
HOST = os.getenv('HOST', "10.179.0.3")
PORT = "3306"
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATA_BASE_NAME}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    quantity = Column(Integer)
    date = Column(Date)



app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# all products
@app.get("/products", response_model=List[dict])
async def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return [{"id": product.product_id, "date": product.date, "price": product.price, "quantity": product.quantity} for product in products]

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
