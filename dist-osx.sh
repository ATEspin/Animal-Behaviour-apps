
PY=python3

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
pyinstaller scripts/Xmaze.py --windowed --onefile

# echo
# echo Cleaning up
# echo
# sleep 1

# # rm -rf build

echo Done
