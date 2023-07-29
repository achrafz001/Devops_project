import uvicorn
from fastapi import FastAPI

app = FastAPI(title = "Photo Converter Service")




@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


















if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    #logger.setLevel(logging.DEBUG)
else:
    #logger.setLevel(gunicorn_logger.level)
    pass