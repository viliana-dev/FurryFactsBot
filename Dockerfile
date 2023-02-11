FROM python:3.8

WORKDIR /app
RUN apt update
RUN apt install -y libgl1-mesa-glx
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "bot.py" ]