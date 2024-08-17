import os
import shutil

APP_DIR = "app"
OUTPUT_DIR = "build"
STATIC_ASSETS = ["CNAME", "index.html"]


def clear_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")


def copy_assets(asset_dirs, output_dir):
    for asset_dir in asset_dirs:
        src_dir = os.path.join(APP_DIR, asset_dir)
        dest_dir = os.path.join(output_dir, asset_dir)

        if os.path.isfile(src_dir):
            shutil.copyfile(src_dir, dest_dir)
        else:
            shutil.copytree(src_dir, dest_dir)


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    clear_directory(OUTPUT_DIR)
    copy_assets(STATIC_ASSETS, OUTPUT_DIR)
