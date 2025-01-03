FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR /src
EXPOSE 8000
RUN python -m pip install --upgrade pip && \
    pip install -r /requirements/development.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home Django_Rest && \
    chown -R Django_Rest:Django_Rest /vol && \
    chmod -R 755 /vol

ENV PATH="/scripts:py/bin:$PATH"

USER Django_Rest

CMD ["run.sh"]