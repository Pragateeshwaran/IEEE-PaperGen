import VideoToAudio
import transcript
import summarization

def start():
    video_path = r"F:\works\A-important\A-neurals\IEEE-PaperGen\I built a GPT Investment Banker using this 312 PAGE document.mp4"
    audio_path = r"F:\works\A-important\A-neurals\IEEE-PaperGen\myAudio.mp3"
    VideoToAudio.video_to_audio(video_path, audio_path)
    logits = transcript.convert(audio_path)
    content = summarization.content_generator(logit=logits['chunks'])
    with open("Content.txt", "w") as f:
        f.write(content)

start()