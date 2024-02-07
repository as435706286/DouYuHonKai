import time
import keyboard


def start_keyboard_listener():
    """
    开始键盘监听的回调函数
    """
    print("Ctrl+Shift+A pressed")
    time.sleep(5)
    # do something


def stop_keyboard_listener():
    """
    停止键盘监听的回调函数
    """
    print("Ctrl+Shift+Q pressed")
    time.sleep(5)
    # do something


# 注册热键，设置回调函数
keyboard.add_hotkey('Ctrl+Shift+A', start_keyboard_listener)
keyboard.add_hotkey('Ctrl+Shift+Q', stop_keyboard_listener)

# 进入监听状态
try:
    keyboard.wait('ctrl+c')
except KeyboardInterrupt:
    ...
