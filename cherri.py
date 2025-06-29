import os
import sys
import subprocess
import shutil
import glob
import json
from typing import Tuple, Optional

parent_dir = os.path.join(os.path.expanduser("~"), "repo", "aapl-cuts")

def get_base_file_name(file_name: str) -> str:
    return os.path.splitext(os.path.basename(file_name))[0]

def get_rename_from_define(file_name: str) -> str:
    with open(file_name, "r") as f:
        for line in f:
            if line.startswith("#define name "):
                return line.strip()[len("#define name "):]
    return get_base_file_name(file_name)

def move_to_shortcuts(shortcut_name, suffix="") -> str:
    src_dir = os.path.join(parent_dir, "src")
    src_path = os.path.join(src_dir, shortcut_name + suffix)
    dest_path = os.path.join(parent_dir, "shortcuts", shortcut_name + suffix)
    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
    return dest_path

def git_add_files(*files):
    try:
        subprocess.run(["git", "add", *files], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding files to git: {e}")

def run_shortcuts(shortcut_name: str):
    testdata_dir = os.path.join(parent_dir, "testdata")
    pattern = os.path.join(testdata_dir, f"{shortcut_name}.in*")
    input_files = glob.glob(pattern)
    if not input_files:
        print(f"No testdata found for shortcut: {shortcut_name}")
        return
    answer = input("Run testdata with this shortcut? (y): ")
    if answer.lower().startswith("n"):
        return

    def use_test_helper_shortcut(input_path: str) -> Tuple[bool, Optional[str]]:
        is_json = input_path.endswith(".json") 
        if is_json:
            # Read the JSON file to determine if it is test_helper input
            with open(input_path, "r") as f:
                try:
                    data = json.load(f)
                    # test_helper.shortcut doesn't overwrite io, so its json input won't have this field
                    json_is_shortcut_input = data.get("overwrite_io", False)
                    # Need to use the correct output type for the test_helper to dump output successfully
                    output_type = data.get("output_type", None)
                    return (not json_is_shortcut_input, output_type)
                except Exception:
                    pass
        return (is_json, None)

    def run_directly(input_path: str, output_path: str):
        # https://support.apple.com/guide/shortcuts-mac/apd455c82f02/mac
        subprocess.run([
            "shortcuts", "run", shortcut_name,
            f"--input-path={input_path}",
            f"--output-path={output_path}",
        ])

    def run_with_test_helper(input_path: str, output_path: str):
        subprocess.run([
            "shortcuts", "run", "test_helper",
            f"--input-path={input_path}",
            f"--output-path={output_path}",
        ])

    def  get_output_and_dest_paths(testdata_dir: str, input_file: str, output_type: Optional[str]) -> Tuple[str, str]:
        output_file = input_file.replace(shortcut_name + ".in", shortcut_name + ".out")
        file_suffix = "." + output_type if output_type else ".txt"
        output_file = os.path.splitext(output_file)[0] + file_suffix
        tmp_dir = os.path.join(testdata_dir, "tmp")
        os.makedirs(tmp_dir, exist_ok=True)
        output_path = os.path.join(tmp_dir, output_file)
        dest_path = os.path.join(testdata_dir, output_file)
        print(f"Constructed output path: {output_path}")
        return output_path, dest_path


    for input_path in input_files:
        file_name = os.path.basename(input_path)
        (use_test_helper, output_type) = use_test_helper_shortcut(input_path)
        output_path, dest_path = get_output_and_dest_paths(testdata_dir, file_name, output_type)
        if use_test_helper:
            run_with_test_helper(input_path, output_path)
        else:
            run_directly(input_path, output_path)
        if not os.path.exists(output_path):
            open(output_path, "w").close()
        if os.path.exists(dest_path):
            subprocess.run(["diff",dest_path, output_path])
        shutil.move(output_path, dest_path)

def main():
    file_name = sys.argv[1]
    git_option = "--git" in sys.argv
    nobuild_option = "--nobuild" in sys.argv

    if not nobuild_option:
        try:
            result = subprocess.run(["cherri", file_name], check=True, text=True)
        except subprocess.CalledProcessError:
            return

    shortcut_name = get_rename_from_define(file_name)
    print(f"Shortcut file: {shortcut_name}")
    shortcut_path = move_to_shortcuts(shortcut_name, ".shortcut")
    xml_path = move_to_shortcuts(shortcut_name, ".xml")
    
    if git_option:
        git_add_files(file_name, shortcut_path, xml_path)
    
    if not nobuild_option:
        subprocess.run(["open", shortcut_path], check=True)
    run_shortcuts(shortcut_name)

if __name__ == "__main__":
    main()