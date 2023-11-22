from sqlalchemy.exc import IntegrityError

from src.services.responses.service_reponse import ServiceResponse


def integrity_error_response(error: str) -> ServiceResponse:
    return ServiceResponse(
        status_code=400,
        content={
            "message": "Ошибка целостности данных",
            "detail": error,
        },
    )


def error_response(error: str) -> ServiceResponse:
    return ServiceResponse(status_code=400, content={"detail": error})
