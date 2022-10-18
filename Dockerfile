FROM python:3.10.8-slim-buster
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD flask --app main.py run
EXPOSE 5000
#CMD whereis python3
