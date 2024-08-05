import os
import subprocess
import re
import sys

# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_highlight(message):
    print(f"{BLUE}{message}{RESET}")

def run_command(command):
    env = os.environ.copy()
    env["DEBIAN_FRONTEND"] = "noninteractive"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, env=env)
    
    output = []
    while True:
        line = process.stdout.readline()
        if not line and process.poll() is not None:
            break
        if line:
            print(line.strip())
            sys.stdout.flush()
            output.append(line)
    
    return ''.join(output), process.returncode

def ask_yes_no(question, default="yes"):
    while True:
        answer = input(f"{question} (Y/n): ").lower().strip()
        if answer == "" or answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        print("Please enter 'y' or 'n', or press Enter for the default.")

def update_system():
    if ask_yes_no("Do you want to update your system?"):
        print_highlight("Updating system...")
        output, return_code = run_command("sudo apt-get update && sudo apt-get upgrade -y")
        
        # Check for lock error
        lock_error_pattern = r"Could not get lock .+. It is held by process \d+ \(apt-get\)"
        if re.search(lock_error_pattern, output):
            print_highlight("Error: Another process is using the package management system.")
            print_highlight("This could be due to an interrupted update or upgrade.")
            if ask_yes_no("Do you want to run 'sudo dpkg --configure -a' to attempt to fix this?"):
                print_highlight("Running 'sudo dpkg --configure -a'...")
                run_command("sudo dpkg --configure -a")
                print_highlight("Retrying system update...")
                output, return_code = run_command("sudo apt-get update && sudo apt-get upgrade -y")

        if return_code != 0:
            print_highlight("Errors encountered during update. Please check the output above.")
        else:
            print_highlight("System update completed successfully.")
    else:
        print_highlight("Skipping system update.")

def fix_broken_packages():
    if ask_yes_no("Do you want to fix broken packages? This may take some time."):
        print_highlight("Fixing broken packages...")
        run_command("sudo apt-get install -f")
        print_highlight("Broken package fix completed.")

def fix_missing_packages():
    if ask_yes_no("Do you want to fix missing packages? This may take some time."):
        print_highlight("Fixing missing packages...")
        run_command("sudo apt-get install --fix-missing")
        print_highlight("Missing package fix completed.")

def upgrade_fix_missing():
    if ask_yes_no("Do you want to upgrade and fix missing packages? This may take a while."):
        print_highlight("Upgrading and fixing missing packages...")
        run_command("sudo apt-get upgrade --fix-missing")
        print_highlight("Upgrade and fix missing completed.")

def upgrade_fix_broken():
    if ask_yes_no("Do you want to upgrade and fix broken packages? This may take a while."):
        print_highlight("Upgrading and fixing broken packages...")
        run_command("sudo apt-get upgrade -f")
        print_highlight("Upgrade and fix broken completed.")

def configure_packages():
    if ask_yes_no("Do you want to configure unconfigured packages? This can be skipped if you ran sudo dpkg --configure -a in the first step. This may take some time."):
        print_highlight("Configuring packages...")
        run_command("sudo dpkg --configure -a")
        print_highlight("Package configuration completed.")

def clean_system():
    if ask_yes_no("Do you want to clean unnecessary packages and cache? This may take a moment."):
        print_highlight("Cleaning system...")
        run_command("sudo apt-get autoremove -y")
        run_command("sudo apt-get autoclean")
        run_command("sudo apt-get clean")
        print_highlight("System cleaning completed.")

def check_disk():
    if ask_yes_no("Do you want to check the disk for errors? This may take a long time."):
        print_highlight("Checking disk for errors...")
        run_command("sudo fsck -f /")
        print_highlight("Disk check completed.")

def repair_filesystem():
    if ask_yes_no("Do you want to check and repair the filesystem? This may take a while."):
        print_highlight("Checking and repairing filesystem...")
        run_command("sudo e2fsck -f -y /dev/sda1")  # Adjust the device name if necessary
        print_highlight("Filesystem check and repair completed.")

def update_grub():
    if ask_yes_no("Do you want to update GRUB? This can help if you're having boot issues."):
        print_highlight("Updating GRUB...")
        run_command("sudo update-grub")
        print_highlight("GRUB update completed.")

def regenerate_font_cache():
    if ask_yes_no("Do you want to regenerate the font cache? This can help with font-related issues."):
        print_highlight("Regenerating font cache...")
        run_command("sudo fc-cache -f -v")
        print_highlight("Font cache regeneration completed.")

def main():
    print_highlight("Welcome to the Kali Linux Repair Script!")
    print_highlight("This script will help you perform various system maintenance tasks.")
    print_highlight("Please note that some tasks may require a significant amount of time.")
    print(f"{YELLOW}                                                                                                                     _  __     _ _   ____                  _        ____            _       _   ")
    print("                                                                                                                    | |/ /__ _| (_) |  _ \ ___ _ __   __ _(_)_ __  / ___|  ___ _ __(_)_ __ | |_ ")
    print("                                                                                                                    | ' // _` | | | | |_) / _ \ '_ \ / _` | | '__| \___ \ / __| '__| | '_ \| __|")
    print("                                                                                                                    | . \ (_| | | | |  _ <  __/ |_) | (_| | | |     ___) | (__| |  | | |_) | |_ ")
    print("                                                                                                                    |_|\_\__,_|_|_| |_| \_\___| .__/ \__,_|_|_|    |____/ \___|_|  |_| .__/ \__|")
    print(f"                                                                                                                                              |_|                                    |_|        {RESET}")

    update_system()
    fix_broken_packages()
    fix_missing_packages()
    upgrade_fix_missing()
    upgrade_fix_broken()
    configure_packages()
    clean_system()
    check_disk()
    repair_filesystem()
    update_grub()
    regenerate_font_cache()

    print_highlight("Kali Linux repair process completed.")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print(f"{RED}This script must be run as root. Please use sudo.{RESET}")
    else:
        main()
