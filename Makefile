all: slides-watch

slides-watch:
	browser-sync start --server --watch

e: edit
edit:
	vim index.html
