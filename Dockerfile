FROM python:3.10.5

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8001

#COPY ./main.py /code/
COPY . /code/
#COPY ./app /code/app

#CMD ["python", "main.py"]