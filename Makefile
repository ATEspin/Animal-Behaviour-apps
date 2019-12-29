
install:
	pip install .

dist-windows:
	bash dist-windows.sh

clean: 
	rm -rf Xmaze.spec dist/ build/

.PHONY=clean dist-windows install