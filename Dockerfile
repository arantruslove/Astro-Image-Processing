FROM python:3.11

WORKDIR /app

# Update and install necessary libraries
RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["tail", "-f", "/dev/null"]
