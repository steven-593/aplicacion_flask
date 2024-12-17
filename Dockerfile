FROM python:3.6-slim

WORKDIR /examen

COPY requirements.txt requirements.txt
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app1.py"]
