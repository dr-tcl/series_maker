FROM python:3.9-slim
LABEL authors="matin"
COPY . /app
WORKDIR /app
RUN pip --timeout=1000 install  -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
