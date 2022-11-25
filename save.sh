docker save -o grafana.tar grafana/grafana:8.2.6
docker save -o influxdb.tar influxdb:2.4.0
docker save -o nodered.tar nodered/node-red:2.2.3
echo "All images have been exported to .tar"
