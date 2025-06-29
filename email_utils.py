# email_utils.py

import re


_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

def is_valid(address):
    return bool(_RE.match(address))

def get_domain(addr):
    # returns everything after the last "@"
    return addr[addr.rfind("@") + 1:]          

def local_part(addr):
    return addr.split("@")[0]                   

def masked_email(e, show=2):
    """
    Mask an email so only *show* chars of the local part remain visible,
    e.g. jo******@example.com
    """
    if not is_valid(e):
        return e                                
    lp, dom = e.split("@")
    masked = lp[:show] + "*" * (len(lp) - show)
    return masked + "@" + dom