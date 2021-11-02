
Test:
Create python script which will accept 4 arguments:
1) Init
 - With this call script should spin-up vagrant host on Centos/Ubuntu/Debian
 - Call ansible playbook to install and configure Grafana, MySQL, Apache, Graphite, Collectd
 - After that Grafana should be available on "https://localhost/grafana/" and show host performance metrics in real-time
2) Stop - stop vagrant box
3) Start - start vagrant box
4) Destroy - destroy vagrant box
Ansible playbook requirements:
1) Grafana
 - Should be configured as a backend for Apache
 - MySQL should be used as Grafana storage
 - Grafana must contain Dashboard with system performance metrics of local vagrant host
 - Dashboard graphs required: CPU LA, CPU Utilization, Memory consumption, Disk performance, Disk consumption(free space), Network bandwidth
 - Dashboard graphs should represent metrics from vagrant host, collected through Collectd + Graphite
 - Dashboard must be available without authentication
2) Graphite
 - Should accept metrics from Collectd on 2003 port
 - Should be available for Grafana as a datasource
3) Apache
 - Should be configured to listen on 443 port with self-signed SSL certificates
 - Grafana needs to be available under /grafana location
Please provide git repo or link on github with task described above
The test is considered passed if we are able to get result through the following commands:
1) git clone https://github.com/username/self-monitor.git
2) python3 ./self-monitor/self-monitor.py init
