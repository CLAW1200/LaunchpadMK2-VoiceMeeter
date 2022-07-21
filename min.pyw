import win32gui, win32con,win32process
Minimize = hwnd = win32gui.FindWindow(None, 'VoiceMeeter.Remote - Macro.Buttons (Version: 1.0.4.0)')
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
