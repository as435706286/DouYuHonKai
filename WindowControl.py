import ctypes
import time

import psutil
import win32api
import win32con
import win32gui
from win32api import *
from win32con import HWND_TOP, SWP_SHOWWINDOW, HWND_TOPMOST, SW_MAXIMIZE
from win32gui import *


def get_window_handle(type=None, title=None):
    """
    通过类名和标题查找窗口句柄.

    Args:
        type(int|None):是否精确搜索. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        int: 返回找到的窗口句柄，如果没有找到则返回0.win32gui.FindWindow(class_name, title)
    """
    # GetDesktopWindow 获得代表整个屏幕的一个窗口（桌面窗口）句柄
    hd = win32gui.GetDesktopWindow()
    # 获取所有子窗口
    hwndChildList = []
    win32gui.EnumChildWindows(hd, lambda hwnd, param: param.append(hwnd), hwndChildList)
    gamehwnd = 0
    if type == 1:
        for hwnd in hwndChildList:
            if title == win32gui.GetWindowText(hwnd):
                gamehwnd = hwnd
    else:
        for hwnd in hwndChildList:
            if title in win32gui.GetWindowText(hwnd):
                gamehwnd = hwnd
    return gamehwnd


def gethandle():
    # 获取当前鼠标【x y】坐标
    time.sleep(2)
    print("2秒内移动鼠标到对应窗口")
    point = win32api.GetCursorPos()
    print(point)

    # 通过坐标获取坐标下的【窗口句柄】
    hwnd = win32gui.WindowFromPoint(point)  # 请填写 x 和 y 坐标
    print(hwnd)

    title = win32gui.GetWindowText(hwnd)
    print('窗口标题:%s' % (title))
    return hwnd


def set_top_window(title=None):
    """
    窗口置顶

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(title=title)
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)


def show_window(title=None):
    """
    显示窗口

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(title=title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)


def hide_window(title=None):
    """
    隐藏窗口

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(title=title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)


def close_window(title=None):
    """
    关闭窗口

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(title=title)
    if hwnd:
        win32gui.CloseWindow(hwnd)


def maximize_window(title=None):
    """
    窗口最大化

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(title=title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


def minimize_window(title=None):
    """
    窗口最小化

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(title=title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)


if __name__ == "__main__":
    # title = '崩坏：星穹铁道'
    # hwnd = get_window_handle(None, title)
    hwnd = gethandle()
    # hwnd = 2756506
    win_title = win32gui.GetWindowText(hwnd)
    print(hwnd,win32gui.GetClassName(hwnd),win_title)

    set_top_window(title=win_title)
    keybd_event(87, 11, 0, 0)
    # keybd_event(87, 11, win32con.KEYEVENTF_KEYUP, 0)
    # show_window(title=win_title)
    # minimize_window(title=win_title)
    # close_window(title=win_title)


