from fabricant import *

def dev():
    env.environment = 'development'
    env.hosts = ['localhost']


def production():
    env.environment = 'production'
    env.hosts = ['amazon']


def setup():
    package_ensure(
        'nginx',
    )

    dir_ensure('/home/art/log/nginx', recursive=True)

    make_symlinks()

    upstart_ensure('nginx')


def deploy():
    local('env/bin/pelican -s {0}.conf content'.format(env.environment))

    if env.environment == 'production':
        local("rsync -avz --exclude .sass-cache --exclude '.*.swp' --exclude 'theme/src' output/ amazon:www/dev.svetlyak/www/")
        local("rsync -avz --exclude '.*.swp' configs/ amazon:www/dev.svetlyak/configs/")
