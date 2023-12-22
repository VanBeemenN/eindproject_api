FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /code
EXPOSE 8000
COPY ./app /app
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./myproject /code/app
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]