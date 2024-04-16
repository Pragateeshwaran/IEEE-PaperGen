import VideoToAudio
import transcript
def start():
    video_path = r"F:\works\A-important\A-neurals\IEEE-PaperGen\₹5 rupees parotta va ah😳‼️🔥 #coimbatore #parotta #food #foodie #ramadan.mp4"
    audio_path = r"F:\works\A-important\A-neurals\IEEE-PaperGen\myAudio.mp3"
    VideoToAudio.video_to_audio(video_path, audio_path)
    logits = transcript.convert(audio_path)
    print(logits)

start()