docker pull docker.elastic.co/elasticsearch/elasticsearch:7.9.2
docker pull docker.elastic.co/kibana/kibana:7.9.2
docker pull docker.elastic.co/logstash/logstash:7.9.2

# tee - redireciona o comando echo em modo sudo para arquivo
echo "vm.max_map_count=12" | sudo tee -a /etc/sysctl.conf
