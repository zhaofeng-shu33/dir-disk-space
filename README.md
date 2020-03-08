This repo is intended to solve the problem of
getting the total size of one directory which
maybe 10TB of size.

# Philosopy
Using native `du` command is time consuming since
the file system uses HDD and loaded as NFS. It brings
a lot of Disk IO and may impact the performance of
other files. Therefore we take a different approach.
We only update statistics of recently modified files
and directories. The problem should be run as a cron
job to get the latest update. To make it actually work,
there are two parameters:

* cron job frequency
* recent updated time

The first parameter should be strictly larger than the
second. For example, if we run the program every day. Then
we can check recent 2 days modified directory or files.

To further accelerated the analysis. We can further cache the
last visit time for one directory. If the time is newer than
the directory, then we do not need to enter the directory again.

