from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from typing import List, Optional
from pydantic import BaseModel, Field
import uuid

# MongoDB Connection URI
MONGODB_URI = "mongodb+srv://vishal:OCx7N1zM66ynIZ6o@cluster12.xhphsya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster12"

# FastAPI App
app = FastAPI() 

# MongoDB Connection
try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    db = client.library
except ServerSelectionTimeoutError:
    raise Exception("Failed to connect to MongoDB.")


# MongoDB Models
class Address(BaseModel):
    city: str
    country: str


class Student(BaseModel):
    name: str
    age: int
    address: Optional[Address] = None
    
# only for checking

##@app.get("/")
##async def root():
  ##  return {"message":"Run Successfully"}


# Routes for Students
@app.post("/students/", response_model=dict)
async def create_student(student: Student):
    student_id = str(uuid.uuid4())  # Generate a UUID for student
    student_data = student.dict(exclude_unset=True)
    student_data["_id"] = student_id  # Add the generated ID to the student data
    collection = db.students
    inserted_student = collection.insert_one(student_data)
    return {"id": student_id}  # Return the ID in the specified format


@app.get("/students/", response_model=dict)
async def get_students():
    collection = db.students
    students = collection.find({}, {"_id": 0, "name": 1, "age": 1})
    return {"data": list(students)}


@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: str):
    collection = db.students
    student = collection.find_one({"_id": student_id})
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")


@app.patch("/students/{student_id}", response_model=dict)
async def update_student(student_id: str, student: Student):
    collection = db.students
    updated_student = collection.update_one({"_id": student_id}, {"$set": student.dict()})
    if updated_student.modified_count == 1:
        return {}
    else:
        raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}", response_model=dict)
async def delete_student(student_id: str):
    collection = db.students
    deleted_student = collection.find_one_and_delete({"_id": student_id})
    if deleted_student:
        return {}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
