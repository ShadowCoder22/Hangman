FROM python:3.3-alpine

WORKDIR /opt/shadowcoder22

ADD hangman.py .

CMD ["python", "hangman.py"]
