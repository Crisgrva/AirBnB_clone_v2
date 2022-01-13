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
sudo echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

# Creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Creating alias for location in nginx conf
sudo chmod 777 /etc/nginx/sites-available/
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

# Restarting nginx
sudo service nginx restart
