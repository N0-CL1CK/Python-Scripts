from fileinput import filename
from sys import argv
from pytube import YouTube

def main(args):
    try:
        video_url = args[0]
        video_quality = args[1]
        stream_obj = YouTube(video_url).streams.filter(res=video_quality, type="video").first()
        if stream_obj:
            stream_obj.download()
        else:
            print("None object was found")
    except IndexError:
        print("Missing arguments")
        print("Necessary <url> and <quality> arguments")
        print("Example: python download_yt_video 'www.youtube.com/videourl' 1080p")

if __name__ == "__main__":
    main(argv[1:])