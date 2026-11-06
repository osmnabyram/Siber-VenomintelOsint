"""Menu olusturma. Cikti orijinal menu() ile ayni gorunumdedir."""

from .colors import WHITE, RED, BOLD, RESET
from .banner import show_banner
from ..core.tools import clear_screen

MENU_ITEMS = [
    (1, "Username Tarama"),
    (2, "E-posta Kontrol (Holehe)"),
    (3, "SocialScan Tarama (S+H)"),
    (4, "BlackBird (Email Taraması)"),
    (5, "BOS"),
    (6, "WhatsMyName"),
    (7, "Photon Web Tarama"),
    (8, "SpiderFoot Baslat"),
    (9, "Shodan"),
    (10, "Maltego"),
    (11, "PYM"),
    (12, "Exiftool"),
    (13, "WaybackMachine"),
]


def show_menu():
    clear_screen()
    show_banner()
    for num, label in MENU_ITEMS:
        print(f"{WHITE}{num}) {label}{RESET}")
    print(f"""{WHITE}
• Tikanirsan Osint Framework{RESET}""")
    print(f"{WHITE}• Tikanirsan epieos.com (Email - Phone){RESET}")
    print(f"""{RED}{BOLD}
0)Cikis{RESET}""")
