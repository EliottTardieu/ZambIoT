docker-compose -f discover_influx.yml down
rm -r data/discover/grafana
rm -r data/discover/influxdb
rm -r data/discover/nodered
cp -r data_backup/discover/grafana data/discover/grafana
cp -r data_backup/discover/influxdb data/discover/influxdb
cp -r data_backup/discover/nodered data/discover/nodered