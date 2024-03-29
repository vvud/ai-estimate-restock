FROM python:3.8

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y install cron

WORKDIR /app

COPY sample_data.json ./
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000
EXPOSE 5000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
