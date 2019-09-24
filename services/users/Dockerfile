# base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# install dependencies
COPY ./app /app
# add and install requirements
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install python-Levenshtein
