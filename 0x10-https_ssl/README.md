# Project name: HTTPS SSL


## Prerequisites
- What is `HTTPS`?
- What are the __2 main elements that SSL is providing__
- `HAProxy` __SSL termination on__ `Ubuntu16.04`
- __SSL termination__
- __Bash function__

## Tasks :heavy_check_mark:

- [0-world_wide_web](./0-world_wide_web)
- [1-haproxy_ssl_termination](./1-haproxy_ssl_termination)
- [100-redirect_http_to_https](./100-redirect_http_to_https)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck (version 0.3.7)` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Installing SSL Termination on Haproxy
- Linux Distro: __Ubuntu 20.04 LTS__
- HAProxy Version: __v2.4.3__

```bash

#if you already have haproxy installed do this
$ sudo snap install --classic certbot

# check if haproxy is installed, if yes stop haproxy
$ sudo service haproxy stop

# Install ssl using certbot
$ sudo certbot certonly --standalone

# Follow the instrustions accurately, at the end please take note of the
# Location of your SSL Keys. Usually going to default to the /etc/letsencrypt
# directory. To view them do the below
$ ls /etc/letsencrypt/live/domain_name/

# Now concat your certificate .pem files to a single pem file and save them to
# /etc/ssl/private
$ cat cert_key_1 cert_key_2 > /etc/ssl/private/any_desired_name.pem

# Now go to your haproxy config file to add a the path to your certificate
# Then reload haproxy
$ sudo service haproxy reload
```
_If you don't have HAProxy installed just copy and run this on your terminal and save yourself the hassle_

```
$ wget -O haproxy https://github.com/sammykingx/alx-system_engineering-devops/raw/master/0x0F-load_balancer/install_haproxy_safely && bash haproxy

```
