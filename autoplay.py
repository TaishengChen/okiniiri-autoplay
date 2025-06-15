import os
import datetime
import subprocess

# 桌面 videos 目录
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
video_dir = os.path.join(desktop, "videos")

# 获取所有视频文件（支持mp4, mov, avi, mkv等，可以自行补充格式）
video_exts = ('.mp4', '.mov', '.avi', '.mkv')
video_files = [f for f in os.listdir(video_dir) if f.lower().endswith(video_exts)]
video_files.sort()
if not video_files:
    raise Exception("没有在桌面videos文件夹下发现任何支持格式的视频文件！")

# 计算今天该播第几个视频
today = datetime.date.today()
idx = today.toordinal() % len(video_files)
video_to_play = os.path.join(video_dir, video_files[idx])

# VLC路径
vlc_path = r"E:\Program Files\VideoLAN\VLC\vlc.exe"   # 改成你实际路径

# 播放到第几个屏幕（扩展屏一般是1或2，自己试试）
screen_number = 1

# 用subprocess运行，避免路径/文件名空格问题
subprocess.run([
    vlc_path,
    video_to_play,
    "--fullscreen",
    "--repeat",
    "--no-video-title-show",
    # f"--screen={screen_number}"
])

