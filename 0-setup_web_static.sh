#!/usr/bin/env bash
# web server configuration for web_static implementation

# Install Nginx
sudo apt update
sudo apt-get -y install nginx
# Adjust the Firewall, allow traffic on port 80
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

sudo echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# Create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
# the program should close correctly (Exit status 0)
exit 0
