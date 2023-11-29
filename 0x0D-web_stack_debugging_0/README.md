# 0x0D Web stack debugging #0 :wrench:
Establish Apache in the container and ensure it responds with a page featuring "Hello Holberton" when querying the root. Once you've connected to the container and addressed any issues, execute the commands to verify that curling port 80 returns a page containing the specified message. Include the commands used to resolve the issue in your response file. After initiating the Docker container, observe that curling port 8080, mapped to the Docker container's port 80, results in an error message. It's worth noting that you may encounter the error message: curl: (52) Empty reply from server.

## Tasks :heavy_check_mark:

0. Bash script that once executed, will bring the webstack to a working state.


## Results :chart_with_upwards_trend:

| Filename |
| ------ |
| [0-give_me_a_page](./0-give_me_a_page)|

## Additional info :construction:
### Resources

- emacs
- BASH
- Debian 9 stable / Ubuntu 16.04 / Ubuntu 18.04 
- Shellcheck
- Puppet 3.8
- Puppet-lint 2.1.1
- Docker

<!
### Try It On Your Machine :computer:
```bash
git clone https://github.com/sammykingx/alx-system_engineering-devops.git
cd 0x0D-web_stack_debugging_0
cat FILENAME
docker run -p 8080:80 -d -it CONTAINER_ID
curl 0:8080
MUST SHOW REPLY FROM SERVER

```
-->

```bash

$ service apache2 start

$ curl localhost

```
