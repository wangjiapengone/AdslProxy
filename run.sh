#!/bin/sh

nohup python3 -u restart_tinyproxy.py > restart.out 2>&1 &
nohup python3 -u run.py > run.out 2>&1 &
