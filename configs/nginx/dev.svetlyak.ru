server {
    listen 80;
    server_name dev.svetlyak.ru;
    access_log /home/art/log/nginx/dev-svetlyak-access.log timed_log;

    location / {
        root /home/art/www/dev.svetlyak/www;
        rewrite ^/favicon.ico$ /theme/img/favicon.ico;
        rewrite ^/robots.txt$  /theme/robots.txt;
        rewrite ^/(.+)/$       /$1.html break;
        rewrite ^/([^/]+)$        /$1/ permanent;
        rewrite ^/(tag|category)/([^/]+)$        /$1/$2/ permanent;
        rewrite ^/feeds/([^.]+)$ http://feeds.feedburner.com/dev-svetlyak/$1;
    }
}

server {
    listen 80;
    server_name aartemenko.com;
    access_log /home/art/log/nginx/aartemenko-access.log timed_log;

    rewrite ^/(texts|links)/$       http://dev.svetlyak.ru/category/$1/ permanent;
    rewrite ^/.*/rss/$              http://dev.svetlyak.ru/feeds/all-en permanent;
    rewrite ^/(texts|links)/(.*)/$  http://dev.svetlyak.ru/$2-en/ permanent;

    rewrite ^/(.*)$          http://dev.svetlyak.ru/$1 permanent;
}

server {
    listen 80;
    server_name code.svetlyak.ru;
    access_log /home/art/log/nginx/code.svetlyak-access.log timed_log;

    rewrite ^/(.*)$          http://dev.svetlyak.ru/$1 permanent;
}
