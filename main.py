import uvicorn
from app.routes import agent, customer, service, timeslot
from fastapi import FastAPI

if __name__ == '__main__':
    uvicorn.run('main:app', port=8001, reload=True)


app = FastAPI()
app.include_router(agent.router)
app.include_router(customer.router)
app.include_router(service.router)
app.include_router(timeslot.router)
