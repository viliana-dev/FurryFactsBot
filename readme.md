The bot could identify the breed of the cat in the picture, as well as provide information about the breed's personality traits, history, and physical characteristics

Model is from https://huggingface.co/spaces/AWP/cat-breed-space

Made by Evgenii Novikov github.com/enovikov11 and Viliana Devbunova github.com/viliana-dev

## How to run

```bash
docker build -t furry-facts-bot .
```

```bash
docker run -d -e "TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE" furry-facts-bot
```
