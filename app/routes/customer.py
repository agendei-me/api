from fastapi import Depends, APIRouter, HTTPException, status, Response
import app
from app.database.postgres_connection import engine, get_session
from app.services.customer import insert_customer
from app.models.customer import Customer, CustomerBase
from sqlmodel import Session

app.models.customer.SQLModel.metadata.create_all(bind=engine)

router = APIRouter(prefix='/customers', )


@router.post("/", response_model=Customer)
def create_agent(customer: CustomerBase, session: Session = Depends(get_session)):
    customer_created = insert_customer(session=session, customer=customer)
    if not customer_created:
        return Response("{'message': 'Customer não pode ser criado'}", status_code=status.HTTP_400_BAD_REQUEST)
    return customer_created
