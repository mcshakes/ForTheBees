FROM python:3.11-slim-bookworm as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/


# RUN pip install --no-cache-dir -r requirements.txt Flask gunicorn


# FROM python:3.11-slim-bookworm

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# COPY --from=builder /app /app

# # CREATE
# RUN useradd -m -u 1000 masterblaster
# # SWITCH TO
# USER masterblaster

# ENV PATH "/app/.local/bin:${PATH}"

# EXPOSE 5000

# ENTRYPOINT ["gunicorn", "main:app", "--bind", "0.0.0.0:8080"]
# CMD []