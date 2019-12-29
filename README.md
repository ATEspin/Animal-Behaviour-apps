# rat-apps

Tools for analysis of rat behavioral experiments.

### Installing

Requires Python 3.  

Once Python 3 is installed, Iistall by installing package with `pip`. In a command line change directories to this folder, ie. one containing `setup.py` and run `pip install .`.  This will install `Xmaze.py` to the Python `Scripts` folder.

### Dist on windows

To create a fodler with .exe files that can be run on any Windows computer without needing to install Python, run the `dist-windows.sh` script using git bash.  ie.
```bash
bash dist-windows.sh
```
or equivalently,
```bash
make dist-windows
```
