def time_conversion(s: str) -> str:
    """Convert 12-hour time like '07:05:45PM' to '19:05:45'."""
    suffix = s[-2:]
    hh = int(s[:2])
    rest = s[2:-2]
    if suffix == "AM":
        if hh == 12:
            return f"00{rest}"
        return f"{s[:2]}{rest}"
    else:  # PM
        if hh == 12:
            return f"{s[:2]}{rest}"
        return f"{hh+12:02d}{rest}"
