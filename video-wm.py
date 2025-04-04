#!/usr/bin/env python3
import os
import subprocess

# Check and create folders if necessary
os.makedirs('originals', exist_ok=True)
os.makedirs('preview', exist_ok=True)

# List video files
videos = [f for f in os.listdir('originals') if f.lower().endswith(('.mp4', '.mov', '.avi'))]

if not videos:
    print("Place your videos in the 'originals' folder")
    exit()

for i, video in enumerate(videos, 1):
    input_file = f'originals/{video}'
    output_file = f'preview/preview-{i:03d}.mp4'
    
    # FFmpeg for pretty good compatibility
    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vf', "drawtext=font=Arial:text='LICENSED':fontsize=24:fontcolor=white@0.3:x=10:y=10",
        '-c:a', 'copy',  # Keep original audio
        '-c:v', 'mpeg4', '-q:v', '3',  # Universal codec
        '-y', output_file
    ]
    
    print(f"Processing {video}...")
    subprocess.run(cmd)

print("All videos processed successfully!")
