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

table = [["Module", "Status"], ["requests", "OK"], ["numpy", "OK"], ["bs4", "OK"]]
print(Fore.CYAN + tabulate(table, headers="firstrow", tablefmt="grid"))

print(Fore.GREEN + "\n[OK] All modules loaded successfully.")
print(Fore.CYAN + "Powered by Arvanex")

