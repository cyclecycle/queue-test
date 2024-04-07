FROM python:3.8-slim

WORKDIR /app

COPY worker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the shared directory
COPY ./shared /app/shared

COPY worker /app

CMD ["python", "tasks.py"]  