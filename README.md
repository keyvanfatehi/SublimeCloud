SublimeCloud
=============

## Description

SublimeCloud is a Sublime Text 2 Plugin which manages your settings, bundle [etc?], installed plugins? via a github repo.

## Future Goals

Allow for different github repo for different projects (how? dot files? Nope, we can use our JSON settings thing... we just need to design it)

## Immediate Goals

* Have our own JSON settings for setting username and password (wait.. how do we ensure this doesn't get synced up to github? check for it specifically because we won't send ourself?)

git ignore? 

## Usage
### Step 1: Seeding the cloud
* I install SublimeCloud plugin
* I open user settings and enter my github username and password (unsafe?)
* I create a hash like this (I'm going to entertain future goal right now):
```json
{
    "username":"foo"
    "password":"asdfasdf" <-- this sucks? what do you think?
    "project_1":"http://path_to_sublimesettings_for_project_1"
    or should it be perhaps like that dot file idea, a .sublime folder?
    "project_1":"http://path_to_sublimesettings_for_project_1/tree/path_to_.sublimefolder"
}
```
* Once I save the file, we check to see if we need to seed the data (is there settings there already?), if we do then we push the current ~/Library/Sublime\ Text\ 2/ to the designated location.

### Step 2: Retreiving your settings
* I install the SublimeCloud plugin
* I create a hash like the above
* When I click save, it will check to see if we have seed data there, if so it will copy into my ~/Library/Sublime\ Text\ 2/ folder