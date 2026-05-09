from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
def room():
    return "Hello Gigi"


if __name__ == "__main__":
    uvicorn run("main:app")