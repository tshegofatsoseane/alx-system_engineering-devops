# 0X0C - Web Server


Web servers consist of hardware and software that use Hypertext Transfer Protocol (HTTP) to respond to web users’ requests made via the World Wide Web.

__NOTE__: In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention).

## Learning Objectives

__General Objectives__
    - what is the main role of a web server
    - What is a child process
    - Why web servers usually have a parent process and child processes
    - What are the main HTTP requests

__DNS__
    - What DNS stands for
    - What is DNS main role

__DNS Record Types__
    - `A Records`
    - `CNAME`
    - `TXT Records`
    - `MX Records`

- How the web works
- `Nginx`
- How to __Configure Nginx__
- Child process concept page
- __Root and sub domain__
- `HTTP` __requests__
- `HTTP` __redirection__
- Not found `HTTP` response code
- Logs files on Linux
- `HTTP/1.1` and `HTTP/2`
- `scp` and `curl`


## Installing Needed Packages

```bash

$ sudo apt-get install shellcheck -y

# Check shellcheck version

$ shellcheck -V

# Installing nginx

$ sudo apt-get install nginx -y

```
## Configuring nginx
```bash

# Configuring the default file

$ sudo vi /etc/nginx/sites-available/default

# Once the vi editior opens

server {
  listen 80 default_Server;
  root /var/www/html;
  index index.html index.htm index.nginx-debian.html;

# if you have a domain name replace '_' with it
  server_name _;

# configuring error_page
  error_page 404 404.html;

  location / {
    try_files $uri $uri/ =404;
  }

  location = /404.html {
    internal;
  }
}

```
