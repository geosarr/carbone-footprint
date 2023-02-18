# Installation and development
- Install the python environment with pip: Install python 3.7, or 3.8 (or 3.9 ?) `pip install -r requirements.txt` after `cd` to the current repository
- Or install it with `conda env create -f environment.yml` after installing `conda` and `cd` to the current repository
- The `Makefile` can be used also to install the requirements with `make all`
- Install `buildozer` to build kivy apps on a Linux platform (follow the instructions at https://buildozer.readthedocs.io/en/latest/installation.html) depending
on the target app (Android, iOS)

# Development
- Modify the app/kivy/buildozer.spec file to fit the new advancements (version, requirements, etc)
- `cd` to app/kivy and run `buildozer android debug deploy` to create .apk file (the android app), it will be in the bin/ folder of app/kivy. Be sure that the buildozer.spec file is in app/kivy folder

# Architecture
Each folder heat, electricity, food, transport is a module containing scripts to train models (if necessary) and do predictions.