
# CI/CD Project README

## Overview

This project is set up to demonstrate a CI/CD pipeline for a Django application. The server is configured to handle requests and serve static and media files.

## Getting Started

1. Clone the repository.
2. Ensure you have Docker and Docker Compose installed.
3. Run `docker-compose up` to start the application.

## Configuration

- The server listens on port 80.
- Adjust the `proxy_pass` directive to match your Django service name.
- Update the paths in the `alias` directives for static and media files as necessary.

## Deployment

Follow the CI/CD pipeline instructions to deploy your application automatically on changes.