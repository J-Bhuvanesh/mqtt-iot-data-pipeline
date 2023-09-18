

FROM python:3.9-slim

WORKDIR /app
RUN python3.9 -m pip install pip --upgrade
COPY . .
RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
