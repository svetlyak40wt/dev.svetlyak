all: devel

reinstall-devel: devel-rm devel

devel-rm:
	rm -fr output
	ssh debian 'rm -fr www/dev.svetlyak/www'

devel: env/bin/pelican
	env/bin/pelican -s devel.conf .
	rsync -avz output/ --exclude .sass-cache --exclude '.*.swp' --exclude 'theme/src' debian:www/dev.svetlyak/www/
	rsync -avz configs/ debian:www/dev.svetlyak/configs/

reinstall-production: production-rm production

production-rm:
	rm -fr output
	ssh locum 'rm -fr www/dev.svetlyak/www'

production: env/bin/pelican
	env/bin/pelican -s production.conf .
	rsync -avz --exclude .sass-cache --exclude '.*.swp' --exclude 'theme/src' output/ locum:www/dev.svetlyak/www/
	rsync -avz --exclude '.*.swp' configs/ locum:www/dev.svetlyak/configs/

env:
	virtualenv env --python=python2.6

env/bin/pelican: env
	env/bin/easy_install pelican
