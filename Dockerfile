FROM python

WORKDIR /uvi

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "alembic upgrade head && gunicorn src.main:app --reload --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:80"]
