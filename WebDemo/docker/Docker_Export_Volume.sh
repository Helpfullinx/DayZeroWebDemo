docker run --rm --volumes-from mysql -v $(pwd)/backup:/backup busybox bin/sh -c "cd /var/lib/mysql && tar -cvf /backup/mysql_volume.tar *"