# espnut Updater
A Windows graphical user interface wrapping [esptool](https://github.com/espressif/esptool) and [mklittlefs](https://github.com/earlephilhower/mklittlefs) solely for flashing image files to espnut devices.

## Building
First build with Qt Creator, then run [nuitka-build.bat](nuitka-build.bat) to compile to standalone binary form.

## Todo
- Flashing FS images without making one first
- I18n
- Error messages in console e.g. tools not found
- Show serial device description
