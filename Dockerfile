FROM python:3.9.23
WORKDIR /main
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]