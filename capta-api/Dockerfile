FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . .

RUN apt-get update \
  && apt-get -y install gcc gnupg2 \
  && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update \
  && ACCEPT_EULA=Y apt-get -y install msodbcsql17 \
  && ACCEPT_EULA=Y apt-get -y install mssql-tools

RUN apt-get -y install unixodbc-dev \
  && apt-get -y install python-pip 

RUN pip install -r requirements.txt
