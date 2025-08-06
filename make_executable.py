#!/usr/bin/env python3
"""
Script to make all shell files in the shell_file directory executable.
Run this once to set up permissions for all shell scripts.
"""

import os
import stat


def ask_permission(prompt):
    """Ask user for permission with y/n prompt"""
    while True:
        response = input(f"{prompt} (y/n): ").lower().strip()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")


def make_all_shell_files_executable():
    """Make all .sh files in shell_file directory executable"""
    shell_folder = "shell_file"

    if not os.path.exists(shell_folder):
        print(f"Directory '{shell_folder}' does not exist.")
        return

    shell_files = [
        f
        for f in os.listdir(shell_folder)
        if f.endswith(".sh") and os.path.isfile(os.path.join(shell_folder, f))
    ]

    if not shell_files:
        print("No shell files found in 'shell_file' directory.")
        return

    print(f"Found {len(shell_files)} shell files:")
    for filename in shell_files:
        print(f"  - {filename}")

    # Ask for bulk permission
    if ask_permission("Do you want to make all shell files executable at once?"):
        print("\nMaking all shell files executable:")
        for filename in shell_files:
            file_path = os.path.join(shell_folder, filename)
            try:
                current_permissions = os.stat(file_path).st_mode
                os.chmod(
                    file_path,
                    current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH,
                )
                print(f"✓ Made {filename} executable")
            except Exception as e:
                print(f"✗ Failed to make {filename} executable: {e}")
        print("\nAll shell files are now executable!")
    else:
        # Ask for individual permissions
        print("\nAsking for individual file permissions:")
        for filename in shell_files:
            file_path = os.path.join(shell_folder, filename)
            if ask_permission(f"Make '{filename}' executable?"):
                try:
                    current_permissions = os.stat(file_path).st_mode
                    os.chmod(
                        file_path,
                        current_permissions
                        | stat.S_IXUSR
                        | stat.S_IXGRP
                        | stat.S_IXOTH,
                    )
                    print(f"✓ Made {filename} executable")
                except Exception as e:
                    print(f"✗ Failed to make {filename} executable: {e}")
            else:
                print(f"✗ Skipped {filename}")


if __name__ == "__main__":
    make_all_shell_files_executable()
