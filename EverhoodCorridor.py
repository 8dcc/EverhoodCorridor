import time, sys, win32gui
from pynput.keyboard import Key, Controller

keyboard = Controller()
dodge_count = 0
match_count = 0

input("\n Will start in 2 seconds. Press any key...")
time.sleep(2)

def passive_ws():
    keyboard.press("w")
    time.sleep(0.1)
    keyboard.release("w")
    time.sleep(0.1)
    keyboard.press("s")
    time.sleep(0.1)
    keyboard.release("s")
    time.sleep(0.1)

def dodge_ws():
    keyboard.release("d")
    time.sleep(0.1)
    keyboard.press("w")
    time.sleep(0.1)
    keyboard.release("w")
    time.sleep(0.1)
    keyboard.press("d")
    time.sleep(0.1)
    keyboard.release("d")
    time.sleep(0.1)
    keyboard.press("s")
    time.sleep(0.1)
    keyboard.release("s")
    time.sleep(0.1)

def get_pixel_colour(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

try:
    pixel_results_390_old = ""
    pixel_results_395_old = ""
    keyboard.press("d")
    while True:
        passive_ws()

        pixel_results_390 = get_pixel_colour(390, 390)
        pixel_results_395 = get_pixel_colour(395, 395)

        sys.stdout.write(f" Dodge count: {dodge_count}  |  Pixel results: {pixel_results_390} - {pixel_results_395}         ")
        sys.stdout.write("\b" * 80)
        sys.stdout.flush()

        if (pixel_results_390 == pixel_results_390_old) and (pixel_results_395 == pixel_results_395_old):
            if (pixel_results_390 != (0, 0, 0)) and (pixel_results_390 != (0, 0, 0)):
                match_count += 1

        if match_count > 3:
            dodge_count += 1
            match_count = 0
            dodge_ws()
            keyboard.press("d")

        pixel_results_390_old = pixel_results_390
        pixel_results_395_old = pixel_results_395

except KeyboardInterrupt:
    keyboard.release("d")
    exit(1)
except Exception as e:
    keyboard.release("d")
    print(f"\n\n {e} \n")
    exit(1)

exit(1)
