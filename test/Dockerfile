FROM python:3.8-slim

WORKDIR /app

COPY test/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./test /app

CMD ["tail", "-f", "/dev/null"]
