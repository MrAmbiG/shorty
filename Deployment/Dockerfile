FROM python:3.6-slim
RUN mkdir shorty
COPY shorty shorty
COPY requirements.txt /
COPY run.sh /
EXPOSE 8001
RUN pip install -r requirements.txt
RUN ls
ENTRYPOINT ["bash","run.sh"]