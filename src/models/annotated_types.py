import datetime
import uuid
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import mapped_column

int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
uuid_pk = Annotated[
    uuid.UUID, mapped_column(primary_key=True, unique=True, default=uuid.uuid4)
]
created_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now(datetime.UTC),
    ),
]
