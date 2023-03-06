# Use the official Python 3.9 image as the base
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the command to run the bot.py file
CMD ["python", "discord_bot.py"]



#docker build -t discord-bot.image .
#docker run -d discord-bot.image