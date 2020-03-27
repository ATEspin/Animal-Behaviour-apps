# Rat-Apps

These are a set of Python-based GUI applications for the analysis of various rat behavioral tests performed for rehabilitation after spinal cord injury.

The programs were written by Abel Torres Espín for analysis at [The Fouad Lab](http://www.rehabresearch.ualberta.ca/karimfouad/about_karim) at the University of Alberta in Edmonton, Alberta.

## Installing

The easiest way to get started is to download pre-bundled versions of the application from [the Github Releases page](https://github.com/cdoolin/rat-apps/releases)



### Installing into existing Python environment

For more advanced users, Rat-Apps can be installed as a module in an existing Python installation. This can reduce the total size of the applications and improve startup time.

Once Python 3 is setup, install with the `pip` command. From a command prompt working in this folder, ie. one containing `setup.py`, run on windows:
```bash
py -3 -m pip install .
```
or on Mac OSX:
```
sudo pip3 install .
```



This will install the `ratapps` module as well as create executable Python scripts for the various apps in the Python scripts directory.  These can then be run by typing the name of the application directly in the console.


**Note: Currently pyqtgraph 0.10 is incompatable with Python 3.8.**  To install the development version of pyqtgraph with Python 3.8, use `pip install git+https://github.com/pyqtgraph/pyqtgraph@develop`

Alternatively, the applications can be run by calling the python module and passing the application name as an argument.  This is more verbose, but may be required if the Python scripts directory is not included in the computers global Path.  To run the module on Windows use:
```bash
py -3 -m ratapps <app>
```
or on Mac OSX:
```bash
python3 -m ratapps <app>
```
Valid applications (`<app>` values) are:
- Xmaze
- Openfield
- Whitebox
- SPGAnalysis



### Bundling Rat-Apps to stand-alone files

The applications can be bundled using [PyInstaller](https://www.pyinstaller.org/) to standalone files whoch can be copied to computers without an existing Python installation.  Pre-built versions of these can be found on [the Github Releases page](https://github.com/cdoolin/rat-apps/releases)

Bundling can be performed with the included `distribute.sh` script, which can be run with
```bash
bash distribute.sh
```
Since this is a bash script, to run on Windows, a bash terminal environment such as the one included with [Git for Windows](https://git-scm.com/download/win) is required.

`distribute.sh` requires an existing Python environment to be available. It uses common default Python commands, but if the `python` executable cannot be found, edit the `distibute.sh` and set the `PY` variable.

When run, `distribute.sh` performs the following:
- Ensures the Python `virtualenv` module is installed
- Creates a new Python virtual environment in this directory and installs Rat-Apps and all requirements to it
- Runs PyInstaller on the applications to generate stand-alone versions.



