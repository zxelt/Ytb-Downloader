# DOC: https://pytube.io/en/latest/
# TO CONVERT TO MP4: https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/



from pytube import YouTube
link = input("URL: ")
YouTube(link).streams.first().download()