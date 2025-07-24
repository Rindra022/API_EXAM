from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.requests import Request
app = FastAPI()
@app.get("/hello")
def greeting():
    return JSONResponse({"message": f"Hello World"}, status_code=200)

@app.get("/welcome")
def welcome_name(name : str):
    return JSONResponse({"message": f"Hello {name}"}, status_code=200)

@app.get("/students")
def list_student():
    return JSONResponse({"message" : serialized_student_list()}, status_code=200)

@app.get("/students-authorized")
def list_student(request: Request):
    auth_header = request.headers.get("Authorization")
    if auth_header:
        return JSONResponse(
            status_code=403,
            content={"error": "Vous n'êtes pas autorisé à accéder à la ressource demandée"}
        )
    if auth_header != "bon courage":
        return JSONResponse(
            status_code=403,
            content={"error": "Vous n'avez pas les permisions necessaires pour accéder à la ressource demandée"}
        )
    return JSONResponse({"message" : serialized_student_list()}, status_code=200)
class StudentModel(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int

student_list: List[StudentModel] = []
def serialized_student_list():
    list_converted = []
    for std in student_list:
        list_converted.append(std.model_dump())
    return list_converted
@app.post("/students")
def add_list_events(events : List[StudentModel]):
    student_list.extend(events)
    return JSONResponse({"message" : serialized_student_list()}, status_code=201)
    # existing_std
@app.put("/students")
def edit_events(students : List[StudentModel]):
    for new_student in students:
        for i, existing_std in enumerate(student_list):
            if existing_std.Reference == new_student.Reference:
                student_list[i] = new_student
                break
            else:
                student_list.append(new_student)
    return {"students": student_list}


