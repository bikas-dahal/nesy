FROM python:3.12.2-slim-bullseye

# Set the working directory in the container

WORKDIR /usr/src/nepstay


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y netcat

# Install dependencies

RUN pip install --upgrade pip

# Copy the dependencies file to the working directory

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .


RUN sed -i 's/\r$//g' /usr/src/nepstay/entrypoint.sh
RUN chmod +x /usr/src/nepstay/entrypoint.sh


# Copy the content of the local src directory to the working directory
COPY . . 


ENTRYPOINT [ "/usr/src/nepstay/entrypoint.sh" ]