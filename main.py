from fastapi import FastAPI, Request
import uvicorn
from app.routes import agent, customer


app = FastAPI()
app.include_router(agent.router)
app.include_router(customer.router)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8001, reload=True)
