from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()
@app.get("/hello")
def greeting():
    return JSONResponse({"message": f"Hello World"}, status_code=200)

