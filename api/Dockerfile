FROM python:3.8-slim

WORKDIR /app

# Install API dependencies
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./shared /app/shared

COPY api /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
