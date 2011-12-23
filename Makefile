all: devel

reinstall-devel: devel-rm devel

devel-rm:
	rm -fr output
	ssh ubuntu 'rm -fr www/dev.svetlyak/www'

devel: env/bin/pelican
	env/bin/pelican -s devel.conf content
	rsync -avz output/ --exclude .sass-cache --exclude '.*.swp' --exclude 'theme/src' ubuntu:www/dev.svetlyak/www/
	rsync -avz configs/ ubuntu:www/dev.svetlyak/configs/

reinstall-production: production-rm production

production-rm:
	rm -fr output
	ssh amazon 'rm -fr www/dev.svetlyak/www'

production: env/bin/pelican
	env/bin/pelican -s production.conf content
	rsync -avz --exclude .sass-cache --exclude '.*.swp' --exclude 'theme/src' output/ amazon:www/dev.svetlyak/www/
	rsync -avz --exclude '.*.swp' configs/ amazon:www/dev.svetlyak/configs/

env:
	virtualenv env --python=python2.6

env/bin/pelican: env
	env/bin/easy_install pelican
