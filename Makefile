
pren:
	uv sync
	uv run tools/00_chat-slicer.py
	uv run ohmyscrapper seed
	uv run ohmyscrapper load
	uv run ohmyscrapper scrap-urls --recursive --randomize --ignore-type
	uv run ohmyscrapper ai --i-am-rich
	uv run tools/01_date-updater.py
	uv run tools/02_archive.py
	uv run tools/03_render.py

render:
	uv run tools/03_render.py

publish:
	rm -rf ~/personal/boulihub/validando.prensadaodevagas.com.br
	cp -a ./public ~/personal/boulihub/validando.prensadaodevagas.com.br
