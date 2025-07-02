#!/bin/bash

PROJECT_DIR="/root/video-subtitle-remover"
INPUT_DIR="$PROJECT_DIR/my-video"

cd "$PROJECT_DIR" || exit 1

echo "=== 开始批量处理任务 (最终修正版) ==="
echo "========================================"
echo ""

shopt -s nullglob nocaseglob

for video_file in "$INPUT_DIR"/*.{mp4,mkv,mov,avi,flv,webm}; do
    filename=$(basename "$video_file")
    echo ""
    echo "--> 正在处理: $filename"

    # 【核心】调用我们自己编写的、干净的 run_process.py 脚本
    python run_process.py "$video_file"

    if [ $? -eq 0 ]; then
        echo "--> ✓ 处理成功: $filename"
    else
        echo "--> X 处理失败: $filename"
    fi
    echo "--------------------------------"
done

shopt -u nullglob nocaseglob

echo ""
echo "=== 所有任务已完成 ==="
