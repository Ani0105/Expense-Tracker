from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./expenses.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ExpenseDB(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    amount = Column(Float)
    category = Column(String)

Base.metadata.create_all(bind=engine)

def add_expense(name: str, amount: float, category: str):
    db = SessionLocal()
    expense = ExpenseDB(name=name, amount=amount, category=category)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    db.close()
    return expense

def get_expenses():
    db = SessionLocal()
    expenses = db.query(ExpenseDB).all()
    db.close()
    return expenses
