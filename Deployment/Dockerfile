FROM python:3.6-buster
RUN mkdir shorty
COPY shorty shorty
COPY requirements.txt /
COPY run.sh /
EXPOSE 8000
RUN pip install --no-cache-dir  -r requirements.txt
ENTRYPOINT ["/bin/bash", "/run.sh"]