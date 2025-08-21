dev:
	npm run dev

build:
	npm run build

test-deploy-chem: public/build/bundle.js
	rsync -av ../build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av ../build/chem/.htaccess reg@www.chem.okayama-u.ac.jp:Sites/test74/pdf
	rsync -av public/ reg@www.chem.okayama-u.ac.jp:Sites/test74

deploy-chem: public/build/bundle.js
	rsync -av ../build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av ../build/chem/.htaccess reg@www.chem.okayama-u.ac.jp:Sites/jscc74/pdf
	rsync -av public/ reg@www.chem.okayama-u.ac.jp:Sites/jscc74
