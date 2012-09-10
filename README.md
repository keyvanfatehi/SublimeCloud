
SublimeCloud
=============

## Description

SublimeCloud is a Sublime Text 2 plugin that syncs your Packages/User directory to/from a github repository. Handy for reinstalling, setting up a new workstation, etc.

### Warnings
* Work in progress
* Pulling is destructive! Please review the code before using.
* Currently if you make a mistake in the git path, you must change it manually, see TODO below

## Todo
* Use sublime_plugin.EventListener to watch for the git repo settings key and update the remote accordingly
* Make it more convenient to use than the command line.
* Have a rubygem or something to faciliate a one-liner for new machines to quickly get your settings

## Installation

* Create a new github repository for my sublime settings to sync to. (Only for first use)

* Ensure push/pull access to said repository.

* Install the plugin by placing the SublimeCloud.py file into ~/Library/Application Support/Sublime Text 2/Packages/User

* Open your user settings in Sublime Text 2 and point the plugin to the github repository

```json
{
    "sublime_cloud_git":"git@github.com:keyvanfatehi/keyvans_sublime_settings.git"
}
```

## Usage (Push)

Use the SublimeCloudPush command to seed the repository with current data:

Open the console with CTRL ~
Enter sublime.run_command("sublime_cloud_push")

## Usage (Pull)

Use the SublimeCloudPull command to replace current data with that on github:

* Open the console with CTRL ~
* Enter sublime.run_command("sublime_cloud_pull")

## Sublime Plugin Reference 

http://docs.sublimetext.info/en/latest/index.html

http://www.sublimetext.com/docs/2/api_reference.html
