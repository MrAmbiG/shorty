FROM python:3.6-buster
RUN mkdir shorty
COPY shorty shorty
COPY requirements.txt /
COPY run.sh /
EXPOSE 8001
RUN pip install -r requirements.txt
ENTRYPOINT ["run.sh"]