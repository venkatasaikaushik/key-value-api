FROM python
COPY key_value_api.py /home/
EXPOSE 5000
RUN pip install flask
RUN pip install gevent
RUN pip install redis
CMD python /home/key_value_api.py
