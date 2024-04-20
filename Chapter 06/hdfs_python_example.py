
from hdfs import InsecureClient
# Connecting to WebHDFS by providing HDFS namenode host and webhdfs port (default 50070)
client = InsecureClient('http://namenode_host:50070', user='hdfs_user')

# Writing Data to HDFS
with open('localfile.txt', 'rb') as file:
    client.write('/user/hdfs_user/hadoopfile.txt', file)

# Reading Data from HDFS
with client.read('/user/hdfs_user/hadoopfile.txt') as reader:
    content = reader.read()
