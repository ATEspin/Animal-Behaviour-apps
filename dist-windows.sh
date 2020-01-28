

# distribute python

PY="py -3"
PYINSTALL_OPTS="--onefile"

echo 
echo Installing Python virtualenv
echo

$PY -m pip install virtualenv
rm -rf dist build
mkdir build

echo
echo Creating new Python virtual environment
echo
sleep 1

$PY -m virtualenv build/venv
source build/venv/scripts/activate

echo
echo Installing requirements
echo
sleep 1

# bug in setuptools 45.0.0
# https://github.com/pypa/setuptools/issues/1963
pip install --upgrade 'setuptools<45.0.0'

pip install . pyinstaller

echo
echo Distributing Xmaze
echo
sleep 1
pyinstaller ratapps/xmaze.py $PYINSTALL_OPTS

echo
echo Distributing SPGanalysis
echo
sleep 1
pyinstaller ratapps/spganalysis.py $PYINSTALL_OPTS

echo
echo Distributing Whitebox
echo
sleep 1
pyinstaller ratapps/whitebox.py $PYINSTALL_OPTS

echo
echo Distributing Openfield
echo
sleep 1
pyinstaller ratapps/openfield.py $PYINSTALL_OPTS

echo
echo Cleaning up
echo
sleep 1

rm -rf build

echo Done