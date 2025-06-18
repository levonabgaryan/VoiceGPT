# Project Setup and Usage Guide

## Prerequisites

Make sure you have **Docker** and **Docker Compose** installed on your machine.

- Follow the official Docker installation guide:  
  [Docker Installation](https://docs.docker.com/engine/install/)

- Follow the official Docker Compose installation guide:  
  [Docker Compose Installation](https://docs.docker.com/compose/install/)

---

## Configuration

1. Create a `.env` file in the project root directory.

2. Copy all environment variables from `env_template` into your `.env` file.

3. Fill in the necessary values for each environment variable.

---

## Build and Run Backend

To build and run the backend service with Docker Compose, run:

```bash
  docker compose up
```

## Frontend Client
There is a simple frontend client included for interacting with the backend:

Open the index.html file in your browser.

Select an MP3 file.

Click the Send to Server button to upload the file and get a response.