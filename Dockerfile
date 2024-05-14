
# Gunakan base image Python
FROM python:3.10

# Set working directory
WORKDIR /app

# Salin file requirements.txt ke dalam kontainer
COPY requirements.txt .

# Instal dependencies
RUN pip install -r requirements.txt

# Salin kode aplikasi ke dalam kontainer
COPY . .

# Jalankan server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

