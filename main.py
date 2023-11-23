# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.database import engine, SessionLocal
from app.db.models import TestTable
from typing import List
app = FastAPI()

# Crear las tablas en la base de datos
TestTable.metadata.create_all(bind=engine)

class TestTableCreate(BaseModel):
    name: str

class TestTableResponse(TestTableCreate):
    id: int

# Endpoint para crear un elemento en la tabla TestTable
@app.post("/create_test_table", response_model=TestTableResponse)
async def create_test_table(test_data: TestTableCreate):
    db = SessionLocal()
    test_instance = TestTable(**test_data.dict())
    db.add(test_instance)
    db.commit()
    db.refresh(test_instance)
    db.close()
    return test_instance

# Endpoint para obtener un elemento por su ID desde la tabla TestTable
@app.get("/get_test_table/{test_id}", response_model=TestTableResponse)
async def get_test_table(test_id: int):
    db = SessionLocal()
    test_instance = db.query(TestTable).filter(TestTable.id == test_id).first()
    db.close()
    if test_instance:
        return test_instance
    raise HTTPException(status_code=404, detail="Item not found")

# Endpoint para actualizar un elemento por su ID en la tabla TestTable
@app.put("/update_test_table/{test_id}", response_model=TestTableResponse)
async def update_test_table(test_id: int, test_data: TestTableCreate):
    db = SessionLocal()
    existing_test = db.query(TestTable).filter(TestTable.id == test_id).first()
    if existing_test:
        for key, value in test_data.dict().items():
            setattr(existing_test, key, value)
        db.commit()
        db.refresh(existing_test)
        db.close()
        return existing_test
    db.close()
    raise HTTPException(status_code=404, detail="Item not found")

# Endpoint para eliminar un elemento por su ID desde la tabla TestTable
@app.delete("/delete_test_table/{test_id}", response_model=TestTableResponse)
async def delete_test_table(test_id: int):
    db = SessionLocal()
    test_instance = db.query(TestTable).filter(TestTable.id == test_id).first()
    if test_instance:
        db.delete(test_instance)
        db.commit()
        db.close()
        return test_instance
    db.close()
    raise HTTPException(status_code=404, detail="Item not found")




# Endpoint para obtener todos los elementos de la tabla TestTable
@app.get("/get_all_test_table", response_model=List[TestTableResponse])
async def get_all_test_table():
    db = SessionLocal()
    test_instances = db.query(TestTable).all()
    db.close()
    return test_instances


# Endpoint para eliminar todos los elementos de la tabla TestTable
@app.delete("/delete_all_test_table")
async def delete_all_test_table():
    db = SessionLocal()
    test_instances = db.query(TestTable).all()
    for test_instance in test_instances:
        db.delete(test_instance)
    db.commit()
    db.close()
    return {"message": "All items have been deleted"}
