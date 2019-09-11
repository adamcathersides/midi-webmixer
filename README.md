# Midi Webmixer

The aim of this project was to allow me to remotely control the 4 aux sends of my Yamaha 01V desk via midi.
The idea being that each of the members in my band can control their own monitor mix on anything that can load a browser (phones etc)

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
* RestAPI 
* GUI (webpage) 

You can run the restapi by itself and access it manually if required (I use the amazing [Insomnia](https://insomnia.rest/) to do this.)
The GUI part relies on the restapi to be running.

## Running the REST api

`webmixer --config config.ini --restapi --port 5001`

## Running the GUI

`webmixer --config config.ini --gui --port 5000`


# Config file

The config file is pretty self explanatory.  As well as normal midi and networking settings, it also allows you to define custom channel names.

The midi port is the number of the midi out port you would like to use.  Find out what you have installed by running `webmix --listmidi` 
If midi port is set to `virtual` the system will create a fake midi port which is handy for debugging.

Here is an example:

```
[Network]
interface = wlp2s0

[Midi]
port = 0

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

# Get midiport numbers

```
webmixer --listmidi
```

# Docker

```
cd midi-webmixer
docker build -t webmixer:1 .
docker run --net=host -v /home/adam/github/01v-midi/config.ini:/config.ini webmixer:1 /config.ini --restapi
docker run --net=host -v /home/adam/github/01v-midi/config.ini:/config.ini webmixer:1 /config.ini --gui
```

# Docker Compose

```
cd midi-webmixer
docker-compose build
docker-compose up
```
