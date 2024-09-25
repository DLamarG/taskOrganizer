docker-compose up -d --build


sleep 5
docker exec taskorganizer-api-1 python /src/manage.py makemigrations
docker exec taskorganizer-api-1 python /src/manage.py migrate 