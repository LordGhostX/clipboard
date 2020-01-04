import win32clipboard as w

def paste():
    w.OpenClipboard()
    d = w.GetClipboardData(w.CF_TEXT)
    w.CloseClipboard()
    return str(d)[2:-1]

def copy(text):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(text, w.CF_TEXT)
    w.CloseClipboard()
