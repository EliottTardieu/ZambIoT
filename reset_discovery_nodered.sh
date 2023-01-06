docker-compose -f discover_nodered.yml down
rm -r data/discover/nodered
cp -r data_backup/discover/nodered data/discover/nodered