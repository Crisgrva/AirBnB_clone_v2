#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static. It must:
# Install NGINX
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# Creating directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Giving Ownership and permissions
sudo chown -R ubuntu:ubuntu /data/

# Creating fake html to test
SIMPLE_HTML="<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"
echo -e "$SIMPLE_HTML" > /data/web_static/releases/test/index.html

# Creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Creating alias for location in nginx conf
sudo chmod 777 /etc/nginx/sites-enabled/
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default

# Restarting nginx
sudo service nginx restart
