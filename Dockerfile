FROM ubuntu:14.04
RUN apt-get update -y
RUN apt-get upgrade -yy
RUN apt-get install python-pip git -y
RUN pip install boto3
RUN pip install pyyaml

