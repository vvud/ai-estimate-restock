FROM python:3.8
# RUN pip install flask
# RUN pip install pymongo
# RUN pip install datetime
# COPY main.py /app/main.py

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY response.json ./

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000
EXPOSE 5000
# CMD ["python", "main.py"]
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
