FROM python:3.8
COPY simple.py /tmp/
CMD ["python", "/tmp/simple.py"]