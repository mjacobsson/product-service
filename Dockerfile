FROM python:3.6
ADD . /home/python
WORKDIR /home/python
RUN pip3 install -r requirements.txt --user
CMD ["./product_service.py"]