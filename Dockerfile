ARG PYTHON_VERSION=3.7-alpine3.16

# the image we want to use
FROM python:${PYTHON_VERSION}
LABEL maintainer="mutuakennedy.crunchgarage.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create our woking directory
RUN mkdir -p /app

# Set created directory as our working directory
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
COPY ./scripts /scripts

RUN set -ex && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    rm -rf /root/.cache/ && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

COPY . .
ENV PATH="/scripts:/py/bin:$PATH"
ENV DJANGO_SETTINGS_MODULE "homey.settings"
USER app

CMD [ "run.sh"]
# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "homey.wsgi"]
