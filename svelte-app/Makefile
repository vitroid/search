build:
	npm run build

test-deploy-chem: public/build/bundle.js
	rsync -av ../build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av ../build/chem/.htaccess reg@www.chem.okayama-u.ac.jp:Sites/test73/
	rsync -av public/ reg@www.chem.okayama-u.ac.jp:Sites/test73

deploy-chem: public/build/bundle.js
	rsync -av ../build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av ../build/chem/.htaccess reg@www.chem.okayama-u.ac.jp:Sites/jscc73/
	rsync -av public/ reg@www.chem.okayama-u.ac.jp:Sites/jscc73
