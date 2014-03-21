
instant-sharing
===
This is a super-simple script lets you instantly share files across a local network with SimpleHTTPServer. See http://www.princeton.edu/~saha/instant-sharing/ for more information.

Installation
---
For the best experience, download share.py and run these commands on a Unix system:

    mv share.py share
    chmod +x share
    cd /usr/local/bin/
    sudo ln -s ~/path/to/share .

Now you're ready to start sharing! Just type the following from any directory on your computer:

    share [port#]
    
For example, you can type:

    share 8000
    
The script will print a link you can share with friends on the local network.