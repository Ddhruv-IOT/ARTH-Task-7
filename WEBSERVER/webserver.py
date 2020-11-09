import os

os.system("yum install httpd -y")
os.system("systemctl start httpd")
os.system("systemctl enable httpd")
os.system("cp index.html /var/www/html")
