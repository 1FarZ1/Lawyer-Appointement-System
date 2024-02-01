FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . .


## expose port
# EXPOSE 8000

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]