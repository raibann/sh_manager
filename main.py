import os
import stat
import sys
import termios
import tty
import asyncio


async def make_executable(file_path):
    """Make a file executable by adding execute permissions"""
    loop = asyncio.get_running_loop()
    current_permissions = await loop.run_in_executor(
        None, lambda: os.stat(file_path).st_mode
    )
    await loop.run_in_executor(
        None,
        lambda: os.chmod(
            file_path, current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
        ),
    )


def getch():
    """Read a single character from stdin (including arrow keys)"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)
        if ch1 == "\x1b":  # Arrow keys
            ch2 = sys.stdin.read(1)
            if ch2 == "[":
                ch3 = sys.stdin.read(1)
                return ch1 + ch2 + ch3
        return ch1
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


async def select_shell_file_radio(folder):
    """Radio-style shell file selector with arrow keys and right-arrow to check, enter to run."""
    loop = asyncio.get_running_loop()
    files = await loop.run_in_executor(
        None,
        lambda: [
            f
            for f in os.listdir(folder)
            if f.endswith(".sh") and os.path.isfile(os.path.join(folder, f))
        ],
    )
    if not files:
        print("No shell files found in 'shell_file' folder.")
        return None

    checked = [False] * len(files)
    idx = 0

    while True:
        clear_screen()
        print("Use ↑/↓ to move, → to select, Enter to run, q to quit.\n")
        for i, fname in enumerate(files):
            cursor = ">" if i == idx else " "
            radio = "[x]" if checked[i] else "[ ]"
            print(f"{cursor} {radio} {fname}")
        print("\nNavigate with arrow keys. Select with →, run with Enter, quit with q.")

        ch = getch()
        if ch == "\x1b[A":  # Up
            idx = (idx - 1) % len(files)
        elif ch == "\x1b[B":  # Down
            idx = (idx + 1) % len(files)
        elif ch == "\x1b[C":  # Right arrow: check this file, uncheck others (radio)
            checked = [False] * len(files)
            checked[idx] = True
        elif ch == "\n" or ch == "\r":  # Enter
            if any(checked):
                return files[checked.index(True)]
            else:
                print("\nPlease select a file with → before running.")
                input("Press Enter to continue...")
        elif ch.lower() == "q":
            return None


async def ask_permission(prompt):
    """Ask user for permission with y/n prompt"""
    while True:
        response = await asyncio.get_event_loop().run_in_executor(
            None, lambda: input(f"{prompt} (y/n): ").lower().strip()
        )
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")


async def main():
    shell_folder = "shell_file"
    selected_fname = await select_shell_file_radio(shell_folder)
    if not selected_fname:
        print("No file selected. Exiting.")
        return

    selected_file = os.path.join(shell_folder, selected_fname)
    print(f"Running: {selected_file}")

    # Ask permission before making the file executable
    if await ask_permission(f"Do you want to make '{selected_fname}' executable?"):
        try:
            await make_executable(selected_file)
            print(f"Made {selected_file} executable")
        except Exception as e:
            print(f"Warning: Could not make file executable: {e}")
    else:
        print("Skipping permission change.")

    try:
        proc = await asyncio.create_subprocess_exec(
            "bash",
            selected_file,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        await proc.communicate()
        if proc.returncode != 0:
            print(f"Error running script: exited with code {proc.returncode}")
    except Exception as e:
        print(f"Error running script: {e}")


if __name__ == "__main__":
    asyncio.run(main())
