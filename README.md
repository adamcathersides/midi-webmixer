# Midi Webmixer

The aim of this project was to allow me to remotely control the 4 aux sends of my Yamaha 01V desk via midi.
The idea being that each of the memebers in my band can control their own monitor mix on anything that can load a browser (phones etc)

# Installation

Clone the repo:
```
git clone git@github.com:adamcathersides/midi-webmixer.git
```

Install
```
cd midi-webmixer
pip install . --user
```

# Running

Once installed the application `webmixer` should be available

The application if comprised to two parts.  
* restapi and the 
* GUI (webpage) 

You can run the restapi by itself and access it manually if required (I use the amazing [Insomnia](https://insomnia.rest/) to do this.
The GUI part relies on the restapi to be running.

## Running the REST api

`webmixer --config config.ini --restapi --port 5001`

## Running the GUI

`webmixer --config config.ini --gui --port 5000`


# Config file

The config file is pretty self explanatory.  As well as normal midi and networking settings, it also allows you to define custom channel channel names.

If midi port is set to `virtual` the system will create a fake midi port which is handy for debugging.

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

