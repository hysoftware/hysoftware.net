# hysoftware.net webapp (WIP)
[![Build Status](https://api.shippable.com/projects/54d80f8e5ab6cc13528b3a5f/badge?branchName=master)](https://app.shippable.com/projects/54d80f8e5ab6cc13528b3a5f/builds/latest)
[![Code Climate](https://codeclimate.com/github/hysoftware/hysoftware.net/badges/gpa.svg)](https://codeclimate.com/github/hysoftware/hysoftware.net)
[![Code Health](https://landscape.io/github/hysoftware/hysoftware.net/master/landscape.svg?style=flat)](https://landscape.io/github/hysoftware/hysoftware.net/master)

## what is this?
This is a web-app of hysoftware.net

## Build instruction

### Requirements
* Python3
* virtualenv
* nodejs
* grunt (install it thru ```npm install -g grunt-cli``` after nodejs is installed)
* bundler (hint: ruby gem...)

### How to (Assume that you already opened prompt)
1. Create a virtualenv and activate it
2. CD into the repo
3. Run ```pip install -r requirements.txt```.
4. Run ```bundle install```.
5. Run ```npm install```.
6. Run ```grunt third_party-dev```

## Development Environment
All build process can be executed through grunt.
The following is the list of commands used for development:

* ```grunt devFront```: Build/Test frontend
* ```grunt devBack```: Build/Test backend
