# Time API

A simple API for getting the current time. You can use this for devices that don't have a clock.

> [!NOTE]
> You can visit the docs for the API at [https://time.dodaucy.com](https://time.dodaucy.com)

## Setup

> [!WARNING]
> Please use the API behind a proxy like [Nginx](https://www.nginx.com/) and set the `Host`, `X-Forwarded-For` and `X-Forwarded-Proto` headers.

1. Clone the repository (Skip this if you have already cloned the repo)

    ```bash
    sudo apt update
    sudo apt install git -y

    git clone https://github.com/dodaucy/time-api.git
    cd time-api
    ```

2. Install Docker

    See [Install Docker Engine](https://docs.docker.com/engine/install/)

3. Build the Docker image

    ```bash
    docker build -t time-api .
    ```

4. Run

    Replace `YOUR_PORT` with the port you configured in the proxy.

    ```bash
    docker run -d -p 127.0.0.1:YOUR_PORT:8000 --restart always --name time-api time-api
    ```

## Local testing

### Prepare

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y

git clone https://github.com/dodaucy/time-api.git  # Skip this if you have already cloned the repo
cd time-api  # Skip this if you have already cloned the repo

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

deactivate
```

### Run

```bash
source venv/bin/activate

python3 -m uvicorn main:app --reload  # Running on http://127.0.0.1:8000

deactivate
```
