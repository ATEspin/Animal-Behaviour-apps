
all:
	@echo run \"make clean\" to clean

clean: 
	rm -rf xmaze.spec openfield.spec spganalysis.spec whitebox.spec dist build

.PHONY=clean all