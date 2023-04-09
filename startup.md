sudo nano /lib/systemd/system/rc-local.service
```sh
[Install] 
WantedBy=multi-user.target 
Alias=rc-local.service
```


sudo nano /etc/rc.local
```sh
#!/bin/sh -e

# run as user
runuser -l dcbot -c 'tmux new-session -d -s bot'

runuser -l dcbot -c 'tmux send-keys -t bot "cd /home/dcbot/dcbot" C-m' 
runuser -l dcbot -c 'tmux send-keys -t bot "python3 main.py" C-m'
#-----------------------------------------------------------
#run as root

tmux new-session -d -s bot

tmux send-keys -t bot "cd /home/dcbot/dcbot" C-m 
tmux send-keys -t bot "python3 main.py" C-m

exit 0
```

sudo chmod +x /etc/rc.local 
sudo systemctl enable rc-local 
sudo systemctl start rc-local 

//optional sudo ln -s /lib/systemd/system/rc-local.service /etc/systemd/system/rc-local.service 

sudo reboot
