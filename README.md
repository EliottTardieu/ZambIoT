# docker-compose-influxdb-grafana-nodered

Multi-container Docker app built from the following services:

* [InfluxDB](https://github.com/influxdata/influxdb) - time series database
* [Node-Red](https://github.com/node-red/node-red) - MQTT UI
* [Grafana](https://github.com/grafana/grafana) - visualization UI for InfluxDB

## Quick Start

To start the app:

1. Install [docker-compose](https://docs.docker.com/compose/install/) on the docker host.
1. Run the following command from the root of the cloned repo **(only for the first time)**:
```
docker compose up --build --remove-orphans
```
1. Run the following command from the root of the cloned repo **(after the first build)**:
```
docker compose up
```

## Ports

The services in the app run on the following ports:

| Host Port | Service |   
| - | - |   
| 3000 | Grafana |   
| 8086 | InfluxDB |   
| 1880 | Node-Red |

## Volumes

Volumes are shared between container and hosting device. The main directory is:  
```{repo-directory}/data```

## Users

The app creates two admin users - one for InfluxDB and one for Grafana. By default, the username and password of both accounts is `admin`. To override the default credentials, set the following environment variables before starting the app:

* `INFLUXDB_USERNAME`
* `INFLUXDB_PASSWORD`
* `GRAFANA_USERNAME`
* `GRAFANA_PASSWORD`

## Database

The app creates a default InfluxDB database called `db0`.

## Data Sources

The app creates a Grafana data source called `InfluxDB` that's connected to the default IndfluxDB database (e.g. `db0`).

To provision additional data sources on start, see the Grafana [documentation](http://docs.grafana.org/administration/provisioning/#datasources) and add a config file to `./grafana-provisioning/datasources/` before starting the app.

## Dashboards

By default, the app will have a visualization dashboard.

To provision additional dashboards on start, see the Grafana [documentation](http://docs.grafana.org/administration/provisioning/#dashboards) and add a config file to `./grafana-provisioning/dashboards/` before starting the app.
