server {
    location / {
        proxy_pass http://0.0.0.0:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Port $server_port;
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        #try_files $uri $uri/ =404;
     }


    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/cat-feeder.pl/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/cat-feeder.pl/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}


server {
    if ($host = cat-feeder.pl) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

if ($host = www.cat-feeder.pl) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    listen [::]:80 ;
    server_name cat-feeder.pl www.cat-feeder.pl;
    return 404; #managed by Certbot
}
