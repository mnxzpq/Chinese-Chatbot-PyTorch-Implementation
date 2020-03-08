FROM python:3.7-slim

ADD . /Chinese-Chatbot-PyTorch-Implementation
WORKDIR /Chinese-Chatbot-PyTorch-Implementation
RUN pip install -r requirements.txt

EXPOSE 10001

ENTRYPOINT ["python3", "rest_server.py"]