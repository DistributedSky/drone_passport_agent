# de_direct

Drone registration agent. It receives the following fields from [the Dapp](https://drone-employee.com/):

* Serial number of the aircraft
* Operator's contact email
* Generic type of drone
* Manufacturer of vehicle
* Model of vehicle
* Country/State registration number of the aircraft
* Operator's full name
* Coutry/State pilot ID

# Pre-setup

In `launch/agent.launch` fill in an email and a password
```
...
<param name="login" value="" /> <!-- Gmail account login -->
<param name="email_from" value="" /> <!-- if it's empty, email_from is equal to login -->
<param name="email_password" value="" /> <!-- Gmail account password -->
...
```

# Build

```
$ nix build -f release.nix
```

# Launch

```
$ source ./result/setup.zsh (bash)
$ roslaunch de_direct agent.launch
```

# NixOS Service

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
