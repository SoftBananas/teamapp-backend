import uuid

from src.services.responses.service_reponse import ServiceResponse


def add_success_response(model_id: int | uuid.UUID) -> ServiceResponse:
    return ServiceResponse(status_code=200, content={"data": {"id": model_id}})
