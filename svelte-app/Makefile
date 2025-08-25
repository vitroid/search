dev:
	npm run dev

build:
	npm run build

HOST=ubuntu@sakutai.net
test-deploy: public/build/bundle.js build
	rsync -av ../build/jscc-access/ $(HOST):.jscc/
	rsync -av ../build/jscc/.htaccess $(HOST):/var/www/html/jscc75/
	rsync -av public/ $(HOST):/var/www/html/jscc75