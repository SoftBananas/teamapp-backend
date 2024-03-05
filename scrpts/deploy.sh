cd teamapp ||
cd mkdir teamapp && cd teamapp && git clone https://github.com/SoftBananas/teamapp-backend.git && git pull

echo "Stop containers"
docker-compose down

echo "Start container"
docker-compose up -d

echo "Finish deploying!"