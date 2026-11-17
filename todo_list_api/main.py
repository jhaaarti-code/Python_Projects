from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()

notes = []

class Note(BaseModel):
    id: int
    title: str
    description: str

app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
def home():
    return FileResponse('static/index.html')
    
@app.post("/notes")
def post_note(note:Note):
    note_data = note.model_dump()
    notes.append (note_data)
    return note_data


@app.get("/notes")
def get_notes():
    return notes

@app.delete("/notes/{note_id}")
def delete_notes(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "note deleted"}
    return {"message": "note not found"}
    
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):
    for index, Existingnote in enumerate(notes):
        if Existingnote["id"] == note_id:
            notes[index] = note.model_dump() # update the note.
            return {"message": "note updated"}
    return {"message": "note not found"}