# BYPopupManager
Easily create excutable popup box with custom message and other machine information for pen testing POC

When doing pen testing, we sometime needs POC executable file for testing such as file upload. BYPopupManager easily let you configure
1. what type of executable file
2. what type of custom popup message to show when get executed
3. what other victim machine information to be put inside the pop up box

Example
=======

Choose executable file feature to be created

![Hello](https://github.com/bayinmin/BYResources/blob/master/BYPopupManager/pic_evil_py.PNG)

File will be created within same folder

![Hello](https://github.com/bayinmin/BYResources/blob/master/BYPopupManager/pic_evil_created.PNG)

The executing result of created file.

![Hello](https://github.com/bayinmin/BYResources/blob/master/BYPopupManager/pic_evil_popup.PNG)

Usage
=====
1. Open command prompt
2. python bypopmanager.py
3. following the instructions on the console

Victim machine information
==========================
Current available information --> hostname

Avaiable excutable extension
============================
Current available extensions:
1. .py
2. .vbs
