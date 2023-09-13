#import pytube libaray 
from pytube import YouTube 
from sys import argv

#argv takes impot from commandline 
# -> allows us to input link straight in commmand line
link = argv[1]
yt = YouTube(link)

#video infromation
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length)