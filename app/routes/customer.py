from fastapi import Depends, APIRouter, HTTPException, status, Response
import app
from app.database.postgres_connection import engine, get_session
from app.services.customer import insert_customer, get_customers
from app.models.customer import Customer, CustomerBase, CustomerWithAgent
from sqlmodel import Session

app.models.customer.SQLModel.metadata.create_all(bind=engine)

router = APIRouter(prefix='/customers', )


@router.post("/", response_model=Customer)
def create_customer(customer: CustomerBase, session: Session = Depends(get_session)):
    return insert_customer(session=session, customer=customer)
    # if not customer_created:
    #     return Response("{'message': 'Customer não pode ser criado'}", status_code=status.HTTP_400_BAD_REQUEST)
    # return customer_created


@router.get("/", response_model=list[CustomerWithAgent])
def read_customers(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    customers = get_customers(session=session, skip=skip, limit=limit)
    return customers
