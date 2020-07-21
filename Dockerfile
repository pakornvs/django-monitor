FROM python:3.7

ARG HOME_DIR=/app

COPY . $HOME_DIR
WORKDIR $HOME_DIR

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput