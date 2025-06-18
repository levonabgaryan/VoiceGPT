FROM python:3.12-slim

ARG package_args="--allow-downgrades --allow-remove-essential --allow-change-held-packages --no-install-recommends"

RUN echo "debconf debconf/frontend select noninteractive" | debconf-set-selections \
  && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -q $package_args update \
  && apt-get -y $package_args upgrade \
  && apt-get -y $package_args install \
        curl \
        build-essential \
        libc-dev \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
