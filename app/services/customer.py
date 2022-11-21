from uuid import uuid4
from app.models.customer import Customer, CustomerBase
from app.models.agent import Agent
from typing import List, Optional
from sqlmodel import select, Session, Relationship


def insert_customer(session: Session, customer: CustomerBase) -> Customer | None:
    db_agent = session.get(Agent, customer.agent_id)

    if db_agent:
        db_customer = Customer(id=str(uuid4()),
                               name=customer.name,
                               plan=customer.plan,
                               whatsapp_number=customer.whatsapp_number,
                               agent_id=db_agent.id)

        session.add(db_customer)
        session.commit()
        session.refresh(db_customer)
        return db_customer


def get_customers(session: Session, skip: int = 0, limit: int = 100) -> list[Customer]:
    customers = session.exec(
                select(
                    Customer
                ).where(
                 Customer.is_active == True
                ).offset(
                    skip
                ).limit(
                    limit
                )
    ).all()
    return customers
