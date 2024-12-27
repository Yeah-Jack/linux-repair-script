# Linux Repair Script

[![DeepSource](https://app.deepsource.com/gh/Yeah-Jack/linux-repair-script.svg/?label=active+issues&show_trend=true&token=BsWVHxHtNGZV40LyyZKWLa8p)](https://app.deepsource.com/gh/Yeah-Jack/linux-repair-script/)
[![CodeFactor](https://www.codefactor.io/repository/github/yeah-jack/linux-repair-script/badge)](https://www.codefactor.io/repository/github/yeah-jack/linux-repair-script)

## Overview

This Linux Repair Script is a comprehensive tool designed to automate various system maintenance and repair tasks for Linux. It provides a user-friendly interface to perform common system upkeep operations, making it easier for beginners and experienced users to maintain their Linux installations.

## Features

- System update and upgrade
- Fixing broken and missing packages
- Configuring unconfigured packages
- System cleaning (removing unnecessary packages and cleaning cache)
- Disk and filesystem checks and repairs
- GRUB update
- Font cache regeneration
- Interactive prompts for each operation
- Real-time output display
- Color-coded messages for better readability

## Requirements

- Linux operating system
- Python 3.x
- Root privileges (sudo access)

## Installation

1. Clone this repository or download the script file:

```bash
git clone https://github.com/Yeah-Jack/Linux-Repair-Script
cd linux-repair-script
```

2. Make the script executable:

```bash
chmod +x linux_repair_script.py
```

## Usage

Run the script with sudo privileges:

```bash
sudo python3 linux_repair_script.py
```

Follow the on-screen prompts to perform various system maintenance tasks. The script will ask for confirmation before executing each task, allowing you to skip operations you don't want to accomplish.

## Caution

This script performs system-level operations. While it's designed to be safe, it's always recommended to back up important data before running system maintenance tools.
- Some operations may take a considerable amount of time, especially on slower systems or with large amounts of data.
- The filesystem repair function (`e2fsck`) is set to check `/dev/sda1` by default. You may need to modify this in the script if your system uses a different partition scheme.

## Contributing

Contributions to improve the script are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This script is released under the MIT License. See the LICENSE file for more details.

## Disclaimer

This script is provided as-is, without any warranties. The authors are not responsible for any data loss or system issues that may occur from using this script. Use at your own risk.
