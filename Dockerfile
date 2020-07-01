FROM python:alpine
ADD . /code
WORKDIR /code
RUN pip install selenium
RUN pip install flask
RUN chmod 644 MainScores.py 
CMD [ "python", "MainScores.py" ]
