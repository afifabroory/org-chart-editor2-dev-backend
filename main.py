from fastapi import FastAPI
from routes.api import endpoint
import uvicorn

app = FastAPI()
app.include_router(endpoint)

if __name__ == '__main__':
    uvicorn.run(app, port=8080)
