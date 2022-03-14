install:
	pyinstaller --onefile pilpdf.py
	sudo mv dist/pilpdf /usr/local/bin/pilpdf
