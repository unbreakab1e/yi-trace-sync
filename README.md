# yi-trace-sync

## What's this

This is a small utility which makes possible to sync videos shot with cheap Xiaomi Yi Action Camera and data from Trace Sports Tracker (http://www.traceup.com/videos).

Trace Sports Tracker is able to sync time on GoPro cameras, but does not care about other ones.
Fortunately, the only thing it does is setting camera's time to current GMT/UTC time.
Yi application, on the other hand, only allows to sync camera's clock to your smartphone clock. So I made this tiny python script.


## Requirements:
* python 2.x/3.x
* correct time on your laptop

## How to use:


* Connect your laptop PC to the camera's WiFi
* Run the script
* You're done!

Note that ideally you'll have to sync time before any riding/recording session.

## Stuff used to make this:

 * https://github.com/vogloblinsky/elmo-qbic-4-cam-rig-manager/blob/master/API_Reverse_engineering.md