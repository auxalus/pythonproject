from fastapi import FastAPI

app = FastAPI(title="project API")

@app.get("/")   # this line creates the html server
def home():
  return{
    "message":"Welcome to project API"
  }

@app.get("/health")
def new():
  return{
    "message":"server is okay"
  }
@app.get("/yash")
def new():
  return{
    "message":"reached"
  }