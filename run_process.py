# run_process.py - Our clean entry point
import sys
import os
import multiprocessing
from backend.main import SubtitleRemover, is_video_or_image

def process_video():
    try:
        multiprocessing.set_start_method("spawn")
    except RuntimeError:
        pass

    if len(sys.argv) < 2:
        print("ERROR: Please provide the video file path as a command-line argument.")
        sys.exit(1)

    video_path = sys.argv[1]

    print(f"--- Clean Runner ---")
    print(f"Received video path: {video_path}")

    if is_video_or_image(video_path):
        print("Path is valid. Creating SubtitleRemover instance...")
        remover_instance = SubtitleRemover(vd_path=video_path, sub_area=None, gui_mode=False)

        print("Instance created. Starting the remover process...")
        remover_instance.run()
        print("Remover process finished for this video.")
    else:
        print(f'ERROR: Invalid video or image path provided: {video_path}')
        sys.exit(1)

if __name__ == '__main__':
    process_video()
