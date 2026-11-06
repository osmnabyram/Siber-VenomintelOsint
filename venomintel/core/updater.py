"""Sessiz otomatik guncelleme (orijinalden korundu).

_SILENT_AUTO_UPDATE_PACKAGES bos oldugundan fiilen hicbir sey yapmaz; mekanizma
orijinaldeki gibi yerinde birakilmistir. Paket eklenirse acilista PyPI'dan surum
kontrol edilip sessizce yukseltilir.
"""

import subprocess
import sys
import time
import json
import urllib.request

_SILENT_AUTO_UPDATE_PACKAGES = {}


def _normalize_ver_silent(v):
    if not v:
        return ()
    parts = []
    for p in v.split("."):
        num = "".join(ch for ch in p if ch.isdigit())
        try:
            parts.append(int(num) if num else 0)
        except Exception:
            parts.append(0)
    return tuple(parts)


def _is_newer_silent(latest, current):
    if latest is None:
        return False
    if current is None:
        return True
    return _normalize_ver_silent(latest) > _normalize_ver_silent(current)


def _get_installed_version_pip_silent(pkg_name):
    try:
        proc = subprocess.run([sys.executable, "-m", "pip", "show", pkg_name],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                              text=True, check=False)
        if proc.returncode != 0 or not proc.stdout:
            return None
        for line in proc.stdout.splitlines():
            if line.startswith("Version:"):
                return line.split(":", 1)[1].strip()
    except Exception:
        return None
    return None


def _get_latest_pypi_version_silent(pkg_name, timeout=4):
    url = f"https://pypi.org/pypi/{pkg_name}/json"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            if resp.status != 200:
                return None
            data = json.load(resp)
            return data.get("info", {}).get("version")
    except Exception:
        return None


def _perform_update_silent(pkg_name):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", pkg_name],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except Exception:
        pass


def silent_auto_update():
    try:
        for _, pkg in _SILENT_AUTO_UPDATE_PACKAGES.items():
            try:
                local = _get_installed_version_pip_silent(pkg)
                latest = _get_latest_pypi_version_silent(pkg)
                if _is_newer_silent(latest, local):
                    _perform_update_silent(pkg)
                time.sleep(0.08)
            except Exception:
                continue
    except Exception:
        pass
