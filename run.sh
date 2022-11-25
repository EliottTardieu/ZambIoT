docker image inspect influxdb:2.4.0 > /dev/null 2>&1 || docker pull influxdb:2.4.0
docker image inspect nodered/node-red:2.2.3 > /dev/null 2>&1 || docker pull nodered/node-red:2.2.3
docker image inspect grafana/grafana:8.2.6 > /dev/null 2>&1 || docker pull grafana/grafana:8.2.6
echo "All images have been loaded. Now starting the docker-compose."
docker-compose up --build --remove-orphans
