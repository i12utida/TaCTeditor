#
# Makefile.tac : C--言語からTacの実行形式に変換する手順
#

TD.exe: TD.cmm
	cm2e -o TD TD.cmm

clean:
	rm -f TD.exe TD.map
