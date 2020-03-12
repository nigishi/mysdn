

from cassandra.cluster import Cluster
cluster = Cluster(['192.168.1.102'])
session = cluster.connect('sample')
rows = session.execute('SELECT id, value FROM t')
for row in rows:
            print(row.id, row.value)
