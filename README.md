# Server monitor challange

## Description

We love our servers and we treat them very well. We would like to have a simple 
script for testing a status of a server, for example: networking, free memory 
and disk space. The script should also be able to send notifications via email, 
slack etc.

Your task is to create a program, which can be executed on a server and 
which performs list of checks. If any of the check fails we want it to send 
notification. List of checks and notification data should be read from a config 
file. For example, in the config file you should be able to specify checks like: 
“ping 8.8.8.8” 
“free_mem 256” 
“free_space /tmp 64” 
“free_space /var/mysql 1024”

and notifications: 
“emails: email@email@com”
“slack access_key room_name”

### My TODO list: 
- [ ] ReadMe 
- [ ] Create config file with server parameters checks list, emails 
list, slack room name
- [ ] Create workers which parse server's logs 
- [ ] Create notifiers which sends notifications (MVP - email and slack msg sender) 
- [ ] Get all together in main script 

### Requirements (for Linux Ubuntu 16.04LTS with Python3.5.2)

Update system
```bash
sudo apt-get update
sudo apt-get upgrade
```

Prepare Python 3.5 env
```bash
sudo apt-get install python3.5
sudo pip3 install virtualenv

(it's my favorite way to manage python's virtualenvs, it's not obligatory or something)
mkdir ~/venvs
cd ~/venvs/

virtualenv django-blog -p $(which python3)
```

Clone repo with https

```bash
cd directory
git clone https://github.com/paniks/blogapp.git
```

Activate virtualenv and install requirements
```bash
(in project dir)

source path/to/venv/bin/activate
pip install -r requiments.txt
```

### Usage

T.B.C.
