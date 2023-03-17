# Raspberry Pi Pico W as a Webserver

The Pico is a cheap and very useful piece of hardware in order to try out and play around with smart home things.

### Here are some steps I did to get started with the Raspberry Pi Pico W as a Webserver

1. Download the latest MicroPython UF2 file from the MicroPython Website: https://datasheets.raspberrypi.com/
    - The file is also in the /assets folder (downloaded on the 16.03.2023)
2. Plug in the Pico into your PC with your thumb pressing the 'BOOSTEL' button
3. Copy the uf2 file on to the device which is now handled as flashdrive
    - The Pico will reboot and then run MicroPython
4. Download and install the Thonny IDE to get started: https://thonny.org/
5. Start Thonny and go to Tools/..Options then selected the Tab 'Interpreter'. 
    - There choose 'MicroPython (Raspberry Pi Pico) as Interpreter
    - Select the detected device as Port (you can also open the DeviceManager in order to find out which number the Pico has)
6. Create files and have fun playing around ;)


## Known Caveats

- `OSError: [Errno 98] EADDRINUSE`
When an error occurs during development with the webserver, you must plug the Pico out and in again.

<br />

### Helpful links:
- https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
- https://datasheets.raspberrypi.com/
- What is MicroPython: https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
- Getting Started with the Pico W: https://how2electronics.com/getting-started-with-raspberry-pi-pico-w-using-micropython/
- Set up a webserver with Pico: https://www.elektronik-kompendium.de/sites/raspberry-pi/2707131.htm
- For use with NFC Tags: https://play.google.com/store/apps/details?id=com.wakdev.nfctools.pro&hl=en
