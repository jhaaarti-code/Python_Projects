from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name: str
    age: int
    grade: str

@app.get("/")
def home():
    return {"message": "Welcome to the Student API"}

@app.get("/aarti")
def get_students():
    return {
        "students": students 
    }
    
@app.post("/student")
def create_student(student:Student):
    students.append(student)
    return {"message " : "student added succesfully" ,
             "students" : student
            }

@app.delete("/student")
def delete_student(student:Student):
    students.remove(student)
    return{" message " : "student deleted successfully" ,
           "students": student
        
    }
    
    
    """
    Create a notes application backend.
    user should be able to:-
    1. Add notes -> with title desc.
    2. See all notes
    3. Delete a particular note
    """
"--1--"
from fastapi import FastAPI
app = FastAPI()

notes = []

@app.post("/notes")
def create_note(note:str):
    note = {
        "notes" : note
    }
    notes.append(note)
    return note

@app.get("/notes")
def get_notes():
    return notes

@app.delete("/notes")
def delete_note():
    notes.pop()
    return {"message" : "note deleted successfully"}

