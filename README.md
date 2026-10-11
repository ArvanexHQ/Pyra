<h1 align="center">Arvanex</h1>

<p align="center">
  <b>A lightweight Python auto-runner for Linux</b><br>
  Detects missing modules, installs them automatically, and runs your script with a clean, colored output.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-Linux-blue?style=for-the-badge&logo=linux&logoColor=white" alt="Platform">
  <img src="https://img.shields.io/badge/language-Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Language">
  <img src="https://img.shields.io/badge/python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License">
</p>

---

## Overview

**Arvanex** is a simple yet powerful command-line tool that takes the pain out of running Python scripts on Linux. Instead of manually installing dependencies every time you run a new script, Arvanex:

- Scans your Python file for imported modules
- Checks which ones are already installed
- Automatically installs any missing ones via `pip`
- Runs your script with a clean, colorful, and organized output

No configuration. No setup. Just run it.

---

## Features

- **Automatic dependency detection** — scans `import` and `from ... import` statements
- **Auto-installation** — installs missing modules with `pip3`
- **Colored output** — clear visual feedback for every step
- **Zero configuration** — works out of the box
- **Lightweight** — pure Bash, no extra dependencies
- **Cross-distro** — works on any Linux with Python 3 and pip3
- **Clean UI** — professional banner and structured logs

---

## Preview

```
  ==============================================
  |                                            |
  |        A R V A N E X                       |
  |                                            |
  |        Python Auto-Runner by Arvanex       |
  |                                            |
  ==============================================

[>] File: test.py
[>] Version: Python 3.11.2
----------------------------------------------
[1/3] Analyzing required modules...
    [OK] requests (installed)
    [>>] bs4 (will be installed)
    [OK] numpy (installed)
[2/3] Installing missing modules...
    > Installing: bs4
    [OK] bs4 installed successfully
[3/3] Running script...
----------------------------------------------

... your script output ...

----------------------------------------------
[OK] Execution completed successfully.
    Developed by Arvanex
----------------------------------------------
```

---

## Installation

### Option 1 — Quick install (recommended)

```bash
git clone https://github.com/ArvanexHQ/arvanex.git
cd arvanex
sudo cp arvanex /usr/local/bin/arvanex
sudo chmod +x /usr/local/bin/arvanex
```

### Option 2 — One-line install

```bash
git clone https://github.com/ArvanexHQ/arvanex.git && cd arvanex && sudo cp arvanex /usr/local/bin/ && sudo chmod +x /usr/local/bin/arvanex
```

### Option 3 — Using the install script

```bash
git clone https://github.com/ArvanexHQ/arvanex.git
cd arvanex
chmod +x install.sh
./install.sh
```

---

## Usage

```bash
arvanex <file.py>
```

### Example

```bash
arvanex test.py
```

That's it. Arvanex will handle the rest.

---

## How It Works

1. **Parse** — reads the target Python file and extracts all top-level imports
2. **Check** — tries to import each module in the current Python environment
3. **Install** — runs `pip3 install` for any module that fails to import
4. **Execute** — runs the script with `python3` and reports the exit code

---

## Requirements

| Requirement | Version |
|-------------|---------|
| Linux       | Any modern distro |
| Bash        | 4.0+    |
| Python      | 3.x     |
| pip3        | Latest  |

Install missing dependencies on Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

On Arch:

```bash
sudo pacman -S python python-pip
```

On Fedora:

```bash
sudo dnf install python3 python3-pip
```

---

## Example Test Script

Save this as `test.py` and run `arvanex test.py`:

```python
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore
import numpy as np
from tabulate import tabulate

colorama.init(autoreset=True)

print(Fore.CYAN + "=" * 50)
print(Fore.CYAN + "     Arvanex Test Script")
print(Fore.CYAN + "=" * 50)

response = requests.get("https://example.com", timeout=10)
print(Fore.GREEN + f"[OK] Status Code: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
print(Fore.YELLOW + f"[>>] Title: {soup.title.string}")

data = np.array([10, 20, 30, 40, 50])
print(Fore.MAGENTA + f"[>>] Sum: {data.sum()} | Mean: {data.mean()}")

table = [["Module", "Status"], ["requests", "OK"], ["numpy", "OK"]]
print(Fore.CYAN + tabulate(table, headers="firstrow", tablefmt="grid"))

print(Fore.GREEN + "\n[OK] All modules loaded successfully.")
print(Fore.CYAN + "Powered by Arvanex")
```

---

## Uninstall

```bash
sudo rm /usr/local/bin/arvanex
```

---

## Roadmap

- [ ] Support for `requirements.txt`
- [ ] Virtual environment integration
- [ ] Package name mapping (e.g. `PIL` → `Pillow`, `cv2` → `opencv-python`)
- [ ] Caching of installed modules
- [ ] `--help` and `--version` flags
- [ ] Windows and macOS support

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Author

**Arvanex**

- GitHub: [@ArvanexHQ](https://github.com/ArvanexHQ)

---

<p align="center">
  <b>Developed by Arvanex</b>
</p>
