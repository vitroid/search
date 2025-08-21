dev:
	npm run dev

build:
	npm run build

HOST=ubuntu@sakutai.net
test-deploy: public/build/bundle.js build ../server.py
	rsync -av public/ $(HOST):test75
	rsync -av ../server.py $(HOST):

# deploy: public/build/bundle.js
# 	rsync -av ../build/chem-access/ $(HOST):.reg/
# 	rsync -av ../build/chem/.htaccess $(HOST):Sites/jscc75/pdf
# 	rsync -av public/ $(HOST):Sites/jscc75
