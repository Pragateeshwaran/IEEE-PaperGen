from moviepy.editor import VideoFileClip

def video_to_audio(video_path, audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    video_clip.close()
    audio_clip.close()

# Example usage
video_path = "F:\works\A important\A neurals\IEEE-PaperGen\₹5 rupees parotta va ah😳‼️🔥 #coimbatore #parotta #food #foodie #ramadan.mp4"
audio_path = "example_audio.mp3"
video_to_audio(video_path, audio_path)
