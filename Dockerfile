FROM python:latest

# Install dependencies.
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Copy code.
ADD dark.py /dark.py

CMD ["python", "/dark.py"]
