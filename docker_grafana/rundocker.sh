docker stop grafana
docker rm grafana
docker run -d -p 3000:3000 -v $PWD/grafanaplugins:/var/lib/grafana -v $PWD/etc/grafana/:/etc/grafana --name=grafana grafana:latest-with-plugins
