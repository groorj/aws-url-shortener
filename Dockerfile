FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app-url-shortener.py .

EXPOSE 8215

CMD ["python", "-u", "app-url-shortener.py"]
