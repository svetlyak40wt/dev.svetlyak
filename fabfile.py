from fabricant import *

def dev():
    env.environment = 'development'
    env.hosts = ['localhost']


def production():
    env.environment = 'production'
    env.hosts = ['svetlyak.ru']


def setup():
    package_ensure(
        'nginx',
    )

    dir_ensure('/home/art/log/nginx', recursive=True)

    make_symlinks()

    upstart_ensure('nginx')


def do_release():
    local('env/bin/pelican -s {0}.conf content'.format(env.environment))

    server = env.hosts[0]
    if env.environment == 'production':
        local("rsync -avz --exclude .sass-cache --exclude '.*.swp' "
              "--exclude 'theme/src' "
              "output/ {0}:www/dev.svetlyak/www/".format(server))
        local("rsync -avz --exclude '.*.swp' "
              "configs/ {0}:www/dev.svetlyak/configs/".format(server))
