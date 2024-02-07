# GetDesktopWindow 获得代表整个屏幕的一个窗口（桌面窗口）句柄
hd = win32gui.GetDesktopWindow()

# 获取所有子窗口
hwndChildList = []
win32gui.EnumChildWindows(hd, lambda hwnd, param: param.append(hwnd), hwndChildList)
gamehwnd = 0
for hwnd in hwndChildList:
    if "剑网3 - " in win32gui.GetWindowText(hwnd):
        gamehwnd = hwnd
        # print(hwnd)
        print("句柄：", hwnd, "标题：", win32gui.GetWindowText(hwnd))
        ShowWindow(hwnd, SW_MAXIMIZE)
    # f.write("句柄：" + str(hwnd) + " 标题：" + win32gui.GetWindowText(hwnd) + '\n')

# hwnd = win32gui.FindWindow(0,win32gui.GetWindowText(265036))#寻找窗口
#
# # win32gui.SetForegroundWindow(gamehwnd)#前置窗口
# ------------------------------------------------------------------
# # 获取桌面窗口句柄
# desktop_hwnd = win32gui.GetDesktopWindow()
#
# # 获取窗口句柄
# hwnd = win32gui.FindWindow(None, "崩坏")
# print(hwnd)
# # 最大化窗口
# ShowWindow(hwnd, SW_MAXIMIZE)