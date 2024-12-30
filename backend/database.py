from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL на базата данни (SQLite)
DATABASE_URL = "sqlite:///./car_management.db"

# Създаване на енджин
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Създаване на сесия
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Декларативна база за модели
Base = declarative_base()
