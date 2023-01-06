docker-compose -f discover_grafana.yml down
rm -r data/discover/grafana
cp -r data_backup/discover/grafana data/discover/grafana