# FastAPI Dockerized API

This repository contains a FastAPI-based API that is containerized using Docker. Below are the steps to build, run, and deploy the application using Docker.

## Table of Contents

- [Requirements](#requirements)


## Requirements

Before you begin, make sure the following software is installed:

- **Docker**: [Docker installation guide](https://docs.docker.com/get-docker/)
- **Python** (if you're testing locally without Docker): [Python installation guide](https://www.python.org/downloads/)

## Installation

### Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/isoume/fast_api_cloud_sql.git
cd fast_api_cloud_sql
`docker build . -t fast_api`<br>
`docker run -d -p 8000:8000 fast_api`<br>
`docker logs <container id>`<br>