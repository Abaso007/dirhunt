from colorama import Fore


def status_code_colors(status_code):
    if 100 <= status_code < 200:
        return Fore.WHITE
    elif status_code == 200:
        return Fore.LIGHTGREEN_EX
    elif 200 < status_code < 300:
        return Fore.GREEN
    elif 300 <= status_code < 400:
        return Fore.LIGHTBLUE_EX
    elif status_code == 500:
        return Fore.LIGHTMAGENTA_EX
    else:
        return Fore.MAGENTA
