FROM tiangolo/uvicorn-gunicorn:python3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/code

COPY requirements.txt .

RUN apt update
RUN apt-get install -y python3-pip build-essential python3-dev default-libmysqlclient-dev pkg-config
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
