# pathfinder
A true pathfinder tool for python.
Have you ever tried to run a single file in a project that is dependent on some modules in the project but python cannot run it
because it can't find those modules, so you have to specify using:
```sh
python -m module.script
```
And then it will run, if the module is present in the cwd.
Or you have to import os, sys in the script and walk back to the root so that it can find the correct path?
Doing this for every time you want to just run the individual file seems tiring.

Pathfinder solves all those problems.
Install it once.
Make sure that the project root contains a .root file and you don't have to worry about anything else.
Just run:  ``` pathfinder <script.py>```.
It doesn't matter where you are in the project, it will run without any issues.

## How it works
-  Automatically detects the project root using a '.root' file in the project root.
-  If you want to make it search the project root with some other file like '.gitignore' or '.env' or '.yaml'
   replace the '.root', or just add your desired file type in the source along with '.root'.
-  Adds all subdirectories to the PYTHONPATH dynamically.

## Installation
### Ubuntu/Linux
1.  Make the file executable:
   ```sh
  chmod +x pathfinder.py
  ```
2.  Move the file for global acces:
  ```sh
  sudo mv pathfinder.py /usr/local/bin/pathfinder
  ```
  If you want to change the name of the executable, replace 'pathfinder' with whatever you want.

### Windows
  At the moment, this doesn't work on windows in the same way it does on linux. If you want, you can try it:
  ```sh
  python pathfinder.py <script.py>
  ```
  I am working on making the file properly executable using already installed python on the system.

## Usage
```sh
pathfinder <script.py> [args...]
```

## Issues
Raise issues if you find any.
