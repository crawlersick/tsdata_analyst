docker build -t grafana:latest-with-plugins \
  --build-arg "GRAFANA_VERSION=latest" \
  --build-arg "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource,grafana-piechart-panel,natel-plotly-panel,ryantxu-ajax-panel,briangann-datatable-panel,jdbranham-diagram-panel,alexanderzobnin-zabbix-app,neocat-cal-heatmap-panel" .
