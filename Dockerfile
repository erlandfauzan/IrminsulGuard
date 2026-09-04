FROM python:3.11-slim

WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Command default untuk running test paralel + generate report
CMD ["python", "-m", "pytest", "-n", "auto", "--html=report.html", "--self-contained-html"]