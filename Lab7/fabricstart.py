from fabric import Connection
c = Connection('22951266-lab7-fabric')

res = c.run('uname -s')
res = c.sudo('service nginx restart')
res = c.sudo('python3 /opt/wwc/mysites/lab/manage.py runserver 8000')
