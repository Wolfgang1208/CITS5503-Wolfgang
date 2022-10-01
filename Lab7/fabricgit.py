from fabric import Connection
c = Connection('22951266-lab7-fabric')
res = c.run('uname -s')
res = c.put('djangosrv','/home/ubuntu/')
res = c.sudo('cp /home/ubuntu/djangosrv /etc/nginx/sites-enabled/')
#res = c.sudo('unlink /etc/nginx/sites-enabled/default')
res = c.run('cat /etc/nginx/sites-enabled/djangosrv')
#res = c.run('git clone https://github.com/Wolfgang1208/opt.git')
#res = c.sudo('cp -r /home/wolfgang/opt /')