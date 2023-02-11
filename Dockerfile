FROM python:3.8

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update
RUN apt install -y libgl1-mesa-glx

CMD [ "python", "bot.py" ]