all: pokeemerald/tools/agbcc
	$(MAKE) -C pokeemerald

pokeemerald/tools/agbcc: ../agbcc/agbcc
	cd ../agbcc; ./install.sh ../generation_3/pokeemerald

../agbcc/agbcc:
	cd ../agbcc; ./build.sh

clean:
	make -C pokeemerald clean
