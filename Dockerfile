# Utiliser une image de base
FROM python:3.8-slim

# Copier les fichiers du site dans le conteneur
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /app
COPY main.py /app/main.py
ARG PASSWORD
ARG HOST
ENV PASSWORD="api"
ENV HOST="10.179.0.3"
RUN echo "The value of PASSWORD is: $PASSWORD"
RUN echo "Host is set to $HOST"
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]