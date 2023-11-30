FROM ubuntu:22.04

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

# python packages install
RUN apt-get update
RUN apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential -y
RUN python3 -m pip install --upgrade pip

# lib install
RUN pip install --no-cache-dir -r requirements.txt

# docker install
RUN apt install -y docker.io

# port number
EXPOSE 7000

# start command
CMD ["sleep", "infinity"]
