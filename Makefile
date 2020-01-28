
install:
	pip install .

dist-windows:
	bash dist-windows.sh

dist-osx:
	bash dist-osx.sh

clean: 
	rm -rf Xmaze.spec dist build

.PHONY=clean dist-windows dist-osx install