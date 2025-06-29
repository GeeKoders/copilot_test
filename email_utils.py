import re

# Improved regex for better email validation precision
_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid(address):
    if not isinstance(address, str):
        return False
    return bool(_RE.fullmatch(address))

def get_domain(addr):
    # returns everything after the last "@"
    if not isinstance(addr, str) or "@" not in addr:
        return ""
    return addr[addr.rfind("@") + 1:]

def local_part(addr):
    if not isinstance(addr, str) or "@" not in addr:
        return ""
    return addr.split("@")[0]

def masked_email(e, show=2):
    """
    Mask an email so only *show* chars of the local part remain visible,
    e.g. jo******@example.com
    """
    if not isinstance(e, str):
        return e
    if not is_valid(e):
        return e
    lp, dom = e.split("@")
    if len(lp) <= show:
        masked = lp
    else:
        masked = lp[:show] + "*" * (len(lp) - show)
    return masked + "@" + dom