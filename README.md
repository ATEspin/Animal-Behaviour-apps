# rat-apps

Tools for analysis of rat behavioral experiments.

### Installing

Requires Python 3.  

Once Python 3 is installed, Iistall by installing package with `pip`. In a command line change directories to this folder, ie. one containing `setup.py` and run `pip install .`.  This will install `Xmaze.py` to the Python `Scripts` folder.

### Dist on windows

To create a folder with .exe files that can be run on any Windows computer without needing to install Python, run the `dist-windows.sh` script using git bash.  ie.
```bash
bash dist-windows.sh
```
or equivalently,
```bash
make dist-windows
```

### Dist on OSX

By default, looks for Python 3 at `/usr/local/bin/python3`, this was to use `brew` Python over Anaconda Python.  If this path is incorrect, edit the top of `dist-osx.sh`.

Then run from this directory
```bash
bash dist-osx.sh
```
or equivalently
```
make dist-osx
```