from pytube import YouTube

def Download(Link):
    ytobj = YouTube(Link)
    ytobj = ytobj.streams.get_highest_resolution()
    try:
        ytobj.download()
    except:
        print(" An Error has Occured ") 
    print("Download is Successful")
    
Link = input("Enter The Youtube Video URL: ")
Download(Link) 

    
    