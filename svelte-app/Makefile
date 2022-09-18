build:
	npm run build

test-deploy-chem: public/build/bundle.js
	rsync -av ../build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av ../build/chem/.htaccess reg@www.chem.okayama-u.ac.jp:Sites/test72
	rsync -av public/ reg@www.chem.okayama-u.ac.jp:Sites/test72

deploy-chem: public/build/bundle.js
	rsync -av ../build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av ../build/chem/.htaccess reg@www.chem.okayama-u.ac.jp:Sites/jscc72
	rsync -av public/ reg@www.chem.okayama-u.ac.jp:Sites/jscc72
