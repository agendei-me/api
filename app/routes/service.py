from fastapi import Depends, APIRouter, HTTPException
import app
from app.database.postgres_connection import engine, get_session
from app.services.service import insert_service, get_service, get_services, update_service, delete_service
from app.models.service import Service, ServiceBase
from sqlmodel import Session

app.models.service.SQLModel.metadata.create_all(bind=engine)

router = APIRouter(prefix='/services', )


@router.post("/", response_model=Service)
def create_agent(service: ServiceBase, session: Session = Depends(get_session)):
    return insert_service(session=session, service=service)


@router.get("/", response_model=list[Service])
def read_agents(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    services = get_services(session=session, skip=skip, limit=limit)
    return services


@router.get("/{service_id}", response_model=Service)
def read_agent(service_id: str, session: Session = Depends(get_session)):
    service = get_service(session=session, service_id=service_id)
    if service is None:
        raise HTTPException(status_code=404, detail='Service not found')
    return service


@router.put("/{service_id}", response_model=Service)
def change_agent(service_id: str, service: ServiceBase, session: Session = Depends(get_session)):
    service = update_service(session=session, service_id=service_id, service=service)
    return service


@router.delete("/{agent_id}")
def remove_agent(service_id: str, session: Session = Depends(get_session)):
    service = delete_service(service_id=service_id, session=session)
    return "{'success': {}}".format(service)
