from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

@app.post("/contact")
async def submit_contact_form(contact: ContactForm):
    return {"message": "Formulário recebido com sucesso!", "data": contact}
