# Rat Apps

These are a set of Python-based GUI applications for the analysis of various rat behavioral tests performed for rehabilitation after spinal cord injury.

The programs were written by Abel Torres Espín for analysis at the Karim Fouad lab at the University of Alberta in Edmonton, Alberta, Canada.

## Installing

The easiest way to get started is to download pre-bundled versions of the application.

### Installing into existing Python environment

Rat-apps can be installed as a module in an existing Python installation. This can reduce the size of the applications and improve startup time.

Once Python 3 is installed, Install by installing package with `pip`. From a command prompt working in this folder, ie. one containing `setup.py` and run, on windows:
```bash
py -3 -m pip install .
```
or on Mac OSX:
```
sudo pip3 install .
```

This will install the `ratapps` module as well as create executable Python scripts for the various apps in the Python scripts directory.  These can then be run by typing the name of the application directly in the console.

Alternatively, the applications can be run by calling the python module and passing the application name as an argument.  This is more verbose, but may be required if the Python `scripts` directory is not included in the computers global Path.  To run via module, on Windows run:
```bash
py -3 -m ratapps <app>
```
or on Max OSX:
```bash
python3 -m ratapps <app>
```
Valid applications (`<app>` values) are:
- Xmaze
- Openfield
- Whitebox
- SPGAnalysis



### Bundling rat-apps to stand-alone files

The applications can be bundled using [PyInstaller](https://www.pyinstaller.org/) to standalone files whoch can be copied to computers without an existing Python installation.

This can be performed with the included `distribute.sh` script, which can be run with
```bash
bash distribute.sh
```
Since this is a bash script, to run on Windows, a bash environment such as the one included with [Git for Windows](https://git-scm.com/download/win) is required.

`distribute.sh` requires an existing Python environment to be available. It uses common default python, but if the Python installer cannot be found, edit the `distibute.sh` and set the `PY` variable.

When run, `distribute.sh` performs the following:
- Ensures `virtualenv` module is installed
- Creates a new Python virtualenvironment in this directory and installs rat-apps and all requirments to it
- Runs PyInstaller on the applications to generate stand-alone versions.



