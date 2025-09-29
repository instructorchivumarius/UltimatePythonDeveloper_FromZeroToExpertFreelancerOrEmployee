# Using pip to Install Packages
# Example with colorama for colored terminal text

from colorama import Fore, Style

print(Fore.RED + "This text is red")
print(Fore.GREEN + "This text is green")
print(Fore.BLUE + "This text is blue")

print(Style.RESET_ALL + "Back to normal")
