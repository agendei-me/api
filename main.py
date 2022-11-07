from dotenv import load_dotenv, find_dotenv
import uvicorn


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    uvicorn.run('main:app', port=8001, reload=True)

from app.routes import agent, customer, service
from fastapi import FastAPI

app = FastAPI()
app.include_router(agent.router)
app.include_router(customer.router)
app.include_router(service.router)
