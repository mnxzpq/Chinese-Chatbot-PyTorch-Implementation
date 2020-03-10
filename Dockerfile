FROM python:3.7-slim

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ADD . /Chinese-Chatbot-PyTorch-Implementation
WORKDIR /Chinese-Chatbot-PyTorch-Implementation
RUN pip install -r requirements.txt
RUN pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
EXPOSE 10001

ENTRYPOINT ["python3", "rest_server.py"]