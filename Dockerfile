# Base Image
FROM python:3.8-slim-buster

# Update APT repository & Install packages
RUN apt-get update

RUN pip3 install python-dotenv requests

RUN mkdir /usr/local/humanode
WORKDIR /usr/local/humanode/

CMD ["/usr/local/humanode/check_node.py","-D"]
