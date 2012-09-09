SublimeCloud
=============

## Description

SublimeCloud is a Sublime Text 2 plugin that syncs your Packages/User directory to/from a github repository. Handy for reinstalling, setting up a new workstation, etc.

## Installation

* I install the SublimeCloud plugin by placing the SublimeCloud.py file in /Users/keyvan/Library/Application Support/Sublime Text 2/Packages/User

* I open my user settings and add my sublime cloud repository git path
```json
{
    "sublime_cloud_repo":"git@github.com:keyvanfatehi/keyvans_sublime_settings.git"
}
```

## Usage (Push)

* I then trigger the SublimeCloudPush command to seed the repository with current data:
  - Check if ~/Library/Application Support/Sublime Text 2/Packages/User is a git repo
    - If not, git init, git commit, and git push (-f) to the sublime_cloud_repo
    - If yes, check if there are uncommitted changes
      - If yes, git init, git commit, git push (-f) to the sublime_cloud_repo
      - If no

## Usage (Pull)

* Or I trigger the SublimeCloudPull command to replace current data with that on github:
  - Check if ~/Library/Application Support/Sublime Text 2/Packages/User is a git repo
    - If not, git init, git commit, and git push (-f) to the sublime_cloud_repo
    - If yes, check if there are uncommitted changes
      - If yes, git init, git commit, git push (-f) to the sublime_cloud_repo
      - If no

## Sublime Plugin Reference 

http://docs.sublimetext.info/en/latest/index.html
http://www.sublimetext.com/docs/api-reference