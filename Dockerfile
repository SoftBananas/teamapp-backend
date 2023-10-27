FROM python:3.12

WORKDIR /teamapp

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "src.main:app", "--workers", "1" , "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
