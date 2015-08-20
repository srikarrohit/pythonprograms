Go through the link https://www.youtube.com/watch?v=3JeHWl0cjJ8
Install Wireshark-used for network analysis
https://ask.wireshark.org/questions/16343/install-wireshark-on-ubuntu
change permission to 755
-------------------------------------------------------------------------------
in input.py

Never use input()
http://stackoverflow.com/questions/1588058/python-read-two-variables-in-a-single-line
raw_input() in 2.7 takes input as string
input() in both taked input as expressions//extra careful
reading variables in a line
--read as a string then split then convert into the necessary datatype and map it to the required number of variables
map(int, raw_input().split())
couldn't log a python session. I guess one can only log in an ipython session
