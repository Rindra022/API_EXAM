from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()
@app.get("/hello")
def greeting():
    return JSONResponse({"message": f"Hello World"}, status_code=200)

@app.get("/welcome")
def welcome_name(name : str):
    return JSONResponse({"message": f"Hello {name}"}, status_code=200)



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
