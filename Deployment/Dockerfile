FROM python:3.6-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir shorty

COPY shorty /shorty
COPY run.sh /

RUN chmod +x /*.sh

# RUN ls -altr

RUN pip install -r /shorty/requirements.txt

RUN ls -altr /shorty

ENTRYPOINT ["python /shorty/manage.py runserver"]
