"""Acilis animasyonu (orijinal loading_animation_with_update ile ayni)."""

import itertools
import os
import sys
import time
from time import sleep

from .colors import MENU_WHITE, GREEN, RESET
from ..core.updater import silent_auto_update


def loading_animation_with_update():
    os.system("clear")
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(f"{MENU_WHITE}Sistem aciliyor ", end="", flush=True)

    updates_done = False
    for _ in range(40):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\b")

        if not updates_done:
            try:
                silent_auto_update()
            except Exception:
                pass
            updates_done = True

    print(f" {GREEN}Hosgeldiniz{RESET}\n")
    sleep(1)
    os.system("clear")
