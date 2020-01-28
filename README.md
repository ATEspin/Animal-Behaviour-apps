# rat-apps

Tools for analysis of rat behavioral experiments.

### Installing

Requires Python 3.  

Once Python 3 is installed, Iistall by installing package with `pip`. In a command line change directories to this folder, ie. one containing `setup.py` and run `pip install .`.  This will install Xmaze.py to the python scripts folder which can then be run.

### Dist


- `pip install virtualenv`
- `virtualenv venv`
- `source venv/scripts/activate`
- `pip install . pyinstaller

### Updating apps for Python 3 + opencv-python
- Add brackets to `print` statements
- `QtGui.QFileDialog.getOpenFileName()` to  `QtGui.QFileDialog.getOpenFileName()[0]`
- `_,cnts,_= cv2.findContours(` to `cnts, _ = cv2.findContours(`
- In `nextFrameSlot()` changed if from
  - `#if nframe < (self.length - 10):` to
  - `if nframe < (self.frame_end - 10):`
  - for timer bug

