FROM python:3.12-slim

#Evita que se actualice el pip
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

#Retrasos al pintar la consola
ENV PYTHONUNBUFFERED=1  

WORKDIR /app

COPY requirements.txt .

#RUN python -m venv venv

#RUN /bin/bash -c "source venv bin/activate"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8002

# Ejecutar la app
CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "8002"]