#!/bin/sh

# 安装tinyproxy
yum install -y epel-release
yum update -y
yum install -y tinyproxy

# 修改tinyproxy文件
sed -i "s/Allow 127.0.0.1/# Allow 127.0.0.1/g" /etc/tinyproxy/tinyproxy.conf

# 启动tinyproxy
systemctl enable tinyproxy.service
systemctl restart tinyproxy.service

# 安装python3
mkdir /home/wang
cd /home/wang
mkdir python3
cd python3
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar -zxvf Python-3.6.5.tgz
mkdir /usr/local/python3
cd Python-3.6.5
./configure --prefix=/usr/local/python3
make && make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

# Python需要安装的库
pip3 install redis requests tornado

# 安装lrzsz
yum install lrzsz