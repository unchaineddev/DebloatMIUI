# Debloat MIUI 

This is a guide on utilizing ADB tools to uninstall packages on your bloated Xiaomi Phone, just so it reduces the spooky tracking from Big Tech, and not hog your system resources for a more minimalistic user experience. 
There's no root required to uninstall these packages. 

***NOTE:*** Running all commands listed in ["command.txt"](/command.txt) will safely remove the applications,yet it is recommended to find a replacement of some 
applications you require. These commands cannot harm your device or put your phone into a loop. However, you may lose functionality of some services like, *_Xiaomi Cloud Services_*, so make sure you don't take out something you need.





## Pre-Requisites for Using ADB on Windows or GNU/Linux (Debian or based)

### Windows Setup :window:


1. Install chocolatey (original steps can be found on chocolatey's website https://chocolatey.org/install)

2. Run Windows powershell as administrator and type the following command: ```Chocolatey choco install adb```


### GNU/Linux Setup :penguin:

Open the terminal and type the following command: ```sudo apt-get install android-tools-adb```


## Setup your Xiaomi Phone for ADB Debugging

1. Open Settings, and select “About Phone”
2. Tap on “MIUI version” seven times
3. Go to Additional Settings, and scroll down to select Developer options
4. Scroll down further and enable “USB debugging” 
5. Plug your device into your computer.
6. On the computer, open up a terminal/command prompt and type ```adb devices```
7. A dialog should appear on your device, asking you to allow USB Debugging. Tap “OK"



## ADB Commands(Works when device is booted)

| Command | Description |
| --- | --- |
adb devices | shows all connected adb devices |
adb shell | launches a shell on the device |
adb reboot | reboots system |
adb shell pm list packages | list all installed packages on the device |
adb install "filename" | installs the given .apk file to your device |
adb uninstall com.package.name | uninstalls package from shell pm list packages |

  
  If you encounter [DELETE_FAILED_INTERNAL_ERROR] while uninstalling packages, bypass it by using: 
  
       adb shell pm uninstall --user 0 <packagename>
  
  ## Find a Package
  
  you can use the following command to list installed packages by name.

    pm list package | grep <package name>

For example, to list all installed packages with Google in their name, you'd type:

    pm list package | grep google

  
  

