FROM python:3.8-slim

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY fetchdata.py /fetchdata.py

ENTRYPOINT ["python", "/fetchdata.py"]