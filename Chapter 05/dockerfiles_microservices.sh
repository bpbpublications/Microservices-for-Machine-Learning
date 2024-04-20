
# Dockerfile for UserService
FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]

# Commands to build Docker images for each service
docker build -t user-service .
docker build -t catalog-service .
docker build -t recommendation-service .
docker build -t analytics-service .
docker build -t api-gateway .
