FROM postgres:10
COPY ./scripts/init_table.sql /docker-entrypoint-initdb.d/init_table.sql


FROM python:3.10
RUN pip3 install --upgrade pip
WORKDIR /app
COPY ./.env ./app/.env
COPY ./requirements.txt ./app/requirements.txt
RUN pip3 install -r ./app/requirements.txt


# # COPY ./data ./app/data
# # COPY ./scripts ./app/scripts
# # EXPOSE "5000"
# # CMD ["python3","app/scripts/csv_to_sql.py", "--host", "0.0.0.0", "--port", "5432"]