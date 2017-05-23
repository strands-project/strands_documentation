The following is needed to ensure that remote hosts can connect to the
control gui:

sudo apt-get install apache2 sudo cp
``rospack find tsc_control_ui``/apache/000-default.conf
/etc/apache2/sites-available/ sudo a2enmod proxy\_wstunnel proxy\_http
proxy\_html rewrite headers sudo service apache2 reload

Setting up remote access to the via a reverse ssh tunnel (or some other
magic I don't understand)

sudo apt-get install proxytunnel autossh

Include this in your ~/.ssh/config (the commented out line is the normal
one when not behind a proxy)

Host harek-tunnel User strands ProxyCommand /usr/bin/proxytunnel -v -p
webcache.cs.bham.ac.uk:3128 -r 194.80.55.142:443 -X -d localhost:22 #
ProxyCommand /usr/bin/proxytunnel -p 194.80.55.142:443 -E -d
localhost:22 Compression yes LocalForward \*:22222 localhost:22
ServerAliveInterval 120 TCPKeepAlive no

autossh -M 32323 strands@harek-tunnel -R32280:localhost:80

sudo ln -s ``rospack find strands_webtools`` /var/www/html/webtools sudo
ln -s ``rospack find tsc_control_ui``/www/\* /var/www/html/


Original page: https://github.com/strands-project/g4s_deployment/blob/indigo-devel/tsc_control_ui/README.md