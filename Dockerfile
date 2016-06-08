FROM ubuntu:14.04
RUN apt-get update -y
RUN apt-get upgrade -yy
RUN apt-get install python-pip git -y
RUN pip install boto3
RUN pip install pyyaml
RUN mkdir /app
COPY start.sh /tmp/start.sh
RUN chmod +x /tmp/start.sh
ENTRYPOINT /tmp/start.sh

