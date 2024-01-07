FROM python:3.12.0-bookworm as python-buster-base

ARG UID=1000
ARG GID=1000

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential libpq-dev

RUN groupadd -g "${GID}" python \
      && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python

ENV POETRY_VENV=/opt/poetry
ENV PATH $POETRY_VENV/bin:$PATH

RUN python3 -m venv $POETRY_VENV && \
    $POETRY_VENV/bin/pip install poetry==1.6.1



FROM python-buster-base as telegram-buster-base
ARG SERVER_PATH
ARG DEV_ENV="main"
ENV DEV_ENV=${DEV_ENV}

COPY /pyproject.toml ./

ENV VIRTUAL_ENV=/app-env
ENV PATH $VIRTUAL_ENV/bin:$PATH

RUN python3 -m venv $VIRTUAL_ENV
RUN poetry install \
        $(echo "--only" $DEV_ENV)



FROM telegram-buster-base as aiogram-bot-buster

WORKDIR ./app
ENV PYTHONPATH /app

RUN chown python:python -R /app

USER python
COPY --chown=python:python . .