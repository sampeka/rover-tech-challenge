FROM python:3.8.2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV PYTHONPATH=$PYTHONPATH:/usr/src/app
ENV PYTHONUNBUFFERED=0

CMD ["python", "-m", "rover"]
