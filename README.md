# Docker Project 1 — Containerized Flask API

A simple Flask API containerized with Docker.

## Features

- Python Flask API
- Docker image
- Environment variables
- Docker healthcheck
- Port mapping
- Docker volumes
- Bind mounts
- Persistent storage

## Endpoints

### /
Returns basic service information.

### /health
Returns application health status.

### /info
Returns environment, version and container hostname.

### /write
Writes a message to persistent storage.

### /read
Reads the stored message.

## Build

```bash
docker build -t docker-project-1 .