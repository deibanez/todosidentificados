# Dockerfile-flask
# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3.7

# Set an environment variable with the directory
# where we'll be running the app
#WORKDIR /usr/src/app
# Create the directory and instruct Docker to operate
# from there from now on
# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir /app
WORKDIR /app
# Expose the port uWSGI will listen on
#EXPOSE 8000
# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.txt
# We copy the rest of the codebase into the image
COPY app.py .
COPY ./templates templates
COPY ./static static

CMD ["gunicorn", "app:app","-b 0.0.0.0:3000","-t 100","--reload"]
