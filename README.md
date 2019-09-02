# ROS-enabled drone passport agent
Example of drone passport registration mechanism based on web3 technologies - Ethereum, IPFS and Robonomics network.

Watch demo on Youtube: [Drone Passport dapp on Ethereum Blockchain](https://youtu.be/LFE_ZJdZCmo) or [Drone Passport agent in action. Terminal view](https://youtu.be/yxGTOkGkBJ8)

## About Distributed Sky project
In order to organize drone operations efficiently, we need to make sure that vehicles have a trusted environment to exchange data and record transactions. 

Drone registration agent. It receives the following fields from [the Dapp](https://drone-employee.com/):

* Contact email 
* Full name
* Pilot ID
* Serial number of a drone
* Registration number
* Generic type of the drone
* Manufacturer of the drone
* Model of the drone

## ROS package details 
### Pre-setup

In `launch/agent.launch` fill in an email and a password
```
...
<param name="login" value="" /> <!-- Gmail account login -->
<param name="email_from" value="" /> <!-- if it's empty, email_from is equal to login -->
<param name="email_password" value="" /> <!-- Gmail account password -->
...
```
You can specify some addresses in the `launch/composer.launch` file

### Build

```
$ nix build -f release.nix
```

### Launch

To launch main agent run:
```
$ source ./result/setup.zsh (bash)
$ roslaunch de_direct agent.launch
```

The composer node is launched via:
```
$ roslaunch de_direct composer.launch
```

### NixOS Service

To start the service as a system service add the following to `/etc/nixos/configuration.nix`:

```
systemd.services.de_direct = {
      requires = [ "roscore.service" ];
      after = ["roscore.service" ]; 
      wantedBy = [ "multi-user.target" ];
      script = ''
        source /root/de_direct/result/setup.bash \
        && roslaunch de_direct agent.launch
      '';
      serviceConfig = {
        Restart = "on-failure";
        StartLimitInterval = 0;
        RestartSec = 60;
        User = "root";
      };
    };
```

and run
```
# nixos-rebuild switch
```

To test the service is up and running:
```
# systemctl status de_direct
```
