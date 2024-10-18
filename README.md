server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://web:8000;  # Change 'web' to your Django service name
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /code/static/;  # Adjust according to your static files path
    }

    location /media/ {
        alias /code/media/;  # Adjust according to your media files path
    }
}
