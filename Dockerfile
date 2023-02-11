FROM python:3.8

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update
RUN apt install -y libgl1-mesa-glx
COPY . .

CMD [ "python", "bot.py" ]