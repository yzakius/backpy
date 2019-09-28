# Backpy

[![Build Status](https://travis-ci.org/yzakius/backpy.svg?branch=master)](https://travis-ci.org/yzakius/backpy)

*A simple backup tool written in python.*

Backpy is just a exercise result of my python learning.

Currently I'm studying "os" module and my purpose is to write a simple backup script.


### Roadmap

- [ ] auto unmount after backup
- [ ] show difference of space in disk after backup
- [x] use command line parameter
- [ ] use a configuration file
- [ ] inform when a destination is not found
- [ ] when running script without source and target, suggest using last valid configuration
- [ ] set list with pattern of files and directories to exclude from backup
- [ ] use libnotify notifications
- [ ] play an audio to indicate the end of the script