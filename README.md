# RaspberryPISniffWifi
树莓派Linux嗅探Wifi信息

一些入门的文档：
- [Aircrack-ng之Airodump-ng命令](https://blog.csdn.net/vevenlcf/article/details/82084633
) 
-  [【无线网络渗透 】如何使用Aircrack-ng 系列工具进行WPA/WPA2的监听和破解](https://blog.csdn.net/vevenlcf/article/details/82084633)
- [python执行系统命令](https://www.cnblogs.com/xuxm2007/archive/2011/01/17/1937220.html)

### 开启监听模式
1. sudo ifconfig wlan0 down
2. sudo iwconfig wlan0 mode Monitor
3. sudo ifconfig wlan0 up

### 关闭监听模式
1. sudo ifconfig wlan0 down
2. sudo iwconfig wlan0 mode Managed
3. sudo ifconfig wlan0 up

