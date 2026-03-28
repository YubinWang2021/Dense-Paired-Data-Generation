import os
import shutil
import glob
import tqdm

def move_pkl_files():
    # ================= 配置路径 =================
    src_dir = "/data/Self-Correction-Human-Parsing/ccvr_image_input_train"
    dst_dir = "/data/Self-Correction-Human-Parsing/ccvr_mid_store_all_pkl_1"

    # 检查源目录是否存在
    if not os.path.exists(src_dir):
        print(f"错误: 源目录不存在: {src_dir}")
        return

    # 创建目标目录 (如果不存在)
    os.makedirs(dst_dir, exist_ok=True)
    print(f"目标目录已准备: {dst_dir}")

    # ================= 查找所有 pkl 文件 =================
    # 使用 glob 匹配所有 .pkl 后缀的文件
    pkl_pattern = os.path.join(src_dir, "*.pkl")
    all_pkl_files = glob.glob(pkl_pattern)

    if not all_pkl_files:
        print("未找到任何 .pkl 文件。")
        return

    print(f"找到 {len(all_pkl_files)} 个 pkl 文件，准备移动...")

    # ================= 开始移动 =================
    success_count = 0
    skip_count = 0
    
    for file_path in tqdm.tqdm(all_pkl_files, desc="Moving PKLs", unit="file"):
        try:
            # 获取文件名
            file_name = os.path.basename(file_path)
            # 构建目标路径
            dst_path = os.path.join(dst_dir, file_name)
            
            # 执行移动操作
            # shutil.move 相当于 Linux 的 mv 命令
            shutil.move(file_path, dst_path)
            success_count += 1
            
        except Exception as e:
            print(f"\n跳过文件 {file_path}: {str(e)}")
            skip_count += 1
            continue

    print(f"\n完成! 成功移动: {success_count}, 跳过: {skip_count}")

if __name__ == "__main__":
    move_pkl_files()