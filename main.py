from fastapi import FastAPI, Request
import uvicorn
from app.routes import agent


app = FastAPI()
app.include_router(agent.router)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8001, reload=True)
