docker-compose -f fully_functional.yml down
rm -r data/grafana
rm -r data/influxdb
rm -r data/nodered
cp -r data_backup/grafana data/grafana
cp -r data_backup/influxdb data/influxdb
cp -r data_backup/nodered data/nodered