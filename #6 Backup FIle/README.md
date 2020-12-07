
Solution 
nmap -p 80 --script=http-backup-finder --script-args http-backup-finder.url=/web-serveur/ch11/index.php challenge01.root-me.org

Các file backup thường là index.php~, index.bak, index.php.bak

http://challenge01.root-me.org/web-serveur/ch11/index.php~


