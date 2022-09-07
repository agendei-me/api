from uuid import uuid4
from app.models.customer import Customer, CustomerBase
from app.models.agent import Agent

from sqlmodel import Session


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
