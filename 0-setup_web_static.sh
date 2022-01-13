#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static. It must:
# Install NGINX
apt-get -y update
apt-get -y install nginx
service nginx start

# Creating directories
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Creating fake html to test
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

# Creating symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving Ownership and permissions
chown -R ubuntu:ubuntu /data/

# Creating alias for location in nginx conf
chmod 777 /etc/nginx/sites-available/
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

# Restarting nginx
service nginx restart
