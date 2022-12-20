from pytube import YouTube
import whisper

yt = YouTube('https://youtube.com/watch?v=MmC-x1NusYU&feature=shares')

video_audio = yt.streams.filter(only_audio=True)


audio = video_audio.download()

model = whisper.load_model("base")
result = model.transcribe(audio)
print(result["text"])