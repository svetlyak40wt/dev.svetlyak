all: devel

devel: env/bin/pelican
	env/bin/pelican -s devel.conf .
	rsync -avz output/ --exclude .sass-cache debian:www/dev.svetlyak/www/
	rsync -avz configs/ debian:www/dev.svetlyak/configs/

production: env/bin/pelican
	env/bin/pelican -s production.conf .
	rsync -avz --exclude .sass-cache --exclude '.*.swp' output/ locum:www/dev.svetlyak/www/
	rsync -avz --exclude '.*.swp' configs/ locum:www/dev.svetlyak/configs/

env:
	virtualenv env --python=python2.6

env/bin/pelican: env
	env/bin/easy_install pelican
