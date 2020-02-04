
#
# distribute.sh
#
# prepares rat-apps for distribution such that they can be copied
# to a new computer without an existing Python installation.
#

# To overide defalt parameters, set the folling variables:
# PY: Command to run python3 with
PY=""
# PYINSTALL_OPTS: Arguments to pass th pyinstaller. 
PYINSTALL_OPTS="--onefile"

VENVACTIVATE="build/venv/bin/activate"

if [[ -z "$PY" ]]; then
    # PY not configured.  Auto-detect.
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Mac OSX detected"
        PY="python3"
        PYINSTALL_OPTS="--windowed --onefile"
    elif [[ "$OSTYPE" == "msys"* ]]; then
        PY="py -3"
        PYINSTALL_OPTS="--onefile"
        VENVACTIVATE="build/venv/scripts/activate"
    else
        echo "Unknown OS detected.  Please manually set PY variable in this script."
        exit 0
    fi
    sleep 1
fi


echo 
echo Installing Python virtualenv
echo

$PY -m pip install --user virtualenv
rm -rf dist build
mkdir build

echo
echo Creating new Python virtual environment
echo
sleep 1

$PY -m virtualenv build/venv
source $VENVACTIVATE

echo
echo Installing requirements
echo
sleep 1

# bug in setuptools 45.0.0
# https://github.com/pypa/setuptools/issues/1963
$PY -m pip install --upgrade 'setuptools<45.0.0'

$PY -m pip install . pyinstaller

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