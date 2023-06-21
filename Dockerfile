FROM python:latest

# Install dependencies.
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Copy code.
ADD light.py /main.py
ADD dark.py /main.py

CMD ["python", "/light.py"]
CMD ["python", "/dark.py"]
