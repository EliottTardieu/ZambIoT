docker-compose -f discover_mosquitto.yml down
rm -r data/discover/mosquitto
cp -r data_backup/discover/mosquitto data/discover/mosquitto