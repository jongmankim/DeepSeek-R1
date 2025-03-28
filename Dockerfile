FROM python

RUN mkdir /myapp
WORKDIR /myapp
ADD . /myapp

RUN pip install -r requirements.txt
CMD ["python", "main.py"]
