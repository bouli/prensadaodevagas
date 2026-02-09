
pren:
	uv run tools/00_chat-slicer.py
	ohmyscrapper seed
	ohmyscrapper load
	ohmyscrapper scrap-urls --recursive --randomize --ignore-type
	ohmyscrapper ai --i-am-rich
	uv run tools/01_date-updater.py
	uv run tools/02_archive.py
	uv run tools/03_render.py

render:
	uv run tools/03_render.py
