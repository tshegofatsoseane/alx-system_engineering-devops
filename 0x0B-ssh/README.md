# SSH Project

In this project, we explore the fundamentals of SSH (Secure Shell) and its usage in connecting to remote servers securely. The project is divided into several tasks, each focusing on different aspects of SSH.

## Task 0: Use a private key

Write a Bash script (0-use_a_private_key) that utilizes SSH to connect to your server using the private key ~/.ssh/school with the username ubuntu. The script should adhere to the specified requirements, using only single-character flags for SSH and avoiding the use of -l.

```bash
#!/usr/bin/env bash

# Use ssh with single-character flags to connect to the server
ssh -i ~/.ssh/school ubuntu@your_server_ip

## Task 1: Create an SSH key pair
Write a Bash script (1-create_ssh_key_pair) that creates an RSA key pair. The private key should be named school, have a key length of 4096 bits, and be protected by the passphrase 'betty'.

```bash
#!/usr/bin/env bash

# Create an RSA key pair
ssh-keygen -t rsa -b 4096 -f ~/.ssh/school -N 'betty'

## Task 2: Client configuration file
Configure your local SSH client with a configuration file (config), ensuring it uses the private key ~/.ssh/school and refuses password authentication.

```bash
# Add the following lines to your SSH client configuration file (~/.ssh/config)

Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no


## Task 3: Let me in!
Add the provided SSH public key to your server's authorized keys file, allowing the user 'ubuntu' to connect using the provided key.

# Append the provided SSH public key to the authorized keys file on the server
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Ka
