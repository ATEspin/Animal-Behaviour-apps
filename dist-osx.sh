
PY=python3

PYINSTALL_OPTS="-windowed -onefile"

echo 
echo Installing Python virtualenv
echo

$PY -m pip install virtualenv --user
rm -rf dist build
mkdir build

echo
echo Creating new Python virtual environment
echo
sleep 1

$PY -m virtualenv build/venv
source build/venv/bin/activate

echo
echo Installing requirements
echo
sleep 1

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
