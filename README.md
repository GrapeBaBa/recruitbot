Recruitbot
==========

Setup development environment
-----------------------------
1. Setup virtualbox and vagrant.
2. Fork the repo https://github.com/GrapeBaBa/recruitbot
3. Clone your forked repo
4. Run vagrant
```shell
cd recuitbot/devenv
vagrant up
```

Run collector
-------------
1. login vagrant
```shell
cd recuitbot/devenv
vagrant ssh
```
2. Setup pygithub
```shell
sudo pip install pygithub
```
3. Run collector
```shell
python /opt/workspace/recruitbot/collector-app/collector/collector.py
```