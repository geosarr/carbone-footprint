# Installation
- Install the python environment with `conda`:
-- `cd` to the current repository
-- `conda env create -f environment.yml`

- The `Makefile` can be used also to install the requirements with `make all` on Linux platform when the command `make` is available.

- Install `buildozer` to build kivy apps on a Linux platform (follow the instructions at https://buildozer.readthedocs.io/en/latest/installation.html) depending
on the target app (Android, iOS)

# Development
- Modify the `src/co2f/app/kivy/buildozer.spec` file to fit the new advancements (version, requirements, etc)

- `cd` to `src/co2f/app/kivy` and run `buildozer android debug deploy` to create `.apk` file (the android app), it will be in the `bin/` folder of `src/co2f/app/kivy`. Be sure that the `buildozer.spec` file is in `src/co2f/app/kivy` folder

# Architecture
Each folder `heating`, `electricity`, `food`, `transport` is a module containing scripts to train models (if necessary) and do predictions.