docker image inspect influxdb:2.4.0 > /dev/null 2>&1 || docker load < influxdb.tar
docker image inspect nodered/node-red:2.2.3 > /dev/null 2>&1 || docker load < nodered.tar
docker image inspect grafana/grafana:8.2.6 > /dev/null 2>&1 || docker load < grafana.tar
echo "All images have been loaded. Now starting the docker-compose."
docker-compose up --build --remove-orphans
