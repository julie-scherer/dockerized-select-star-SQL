FROM python:3.10
WORKDIR /app/
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "./scripts/csv_to_sql.py"]

# docker build -t star-select .
# docker run star-select