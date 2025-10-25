FROM python:3.11-trixie

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc pkg-config default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirments.txt  requirments.txt
RUN pip install --no-cache-dir -r requirments.txt

COPY wait-for-db.sh /app/wait-for-db.sh
RUN chmod +x /app/wait-for-db.sh

COPY . .

# Collect static files inside the image
RUN python manage.py collectstatic --noinput || echo "Skipping collectstatic"

EXPOSE 8000

# ENTRYPOINT ["python3"]
CMD ["sh", "-c", "./wait-for-db.sh && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]