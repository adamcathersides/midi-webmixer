# Midi Webmixer

The aim of this project was to allow me to remotely control the 4 aux sends of my Yamaha 01V desk via midi.
The idea being that each of the memebers in my band can control their own monitor mix on anything that can load a browser (phones etc)

# Config file

The config file is pretty self explanatory.  As well as normal midi and networking settings, it also allows you to define custom channel channel names.

If midi port is set to virtual the system will create a fake midi port which is handy for debugging.

Here is an example:

```
[Network]
interface = wlp2s0

[Midi]
port = virtual

[ChannelNames]
1 = Kick
2 = Snare
3 = Hats
4 =
5 =
6 =
7 =
8 =
9 =
10 =
11 =
12 =
```

