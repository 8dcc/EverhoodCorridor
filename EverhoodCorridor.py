import time, sys
from pynput.keyboard import Key, Controller

keyboard = Controller()
count = 0
meta_count = 0

input("\n Will start in 2 seconds. Press any key...")
time.sleep(2)

def w_s():
    keyboard.press("w")
    time.sleep(0.1)
    keyboard.release("w")
    time.sleep(0.1)
    keyboard.press("s")
    time.sleep(0.1)
    keyboard.release("s")
    time.sleep(0.1)

try:
    keyboard.press("d")
    while True:
        w_s()

        if count > 30:
            meta_count += 1
            sys.stdout.flush()
            sys.stdout.write(f"\r Reached the 30 mark {meta_count} times.")
            count = 0
            keyboard.release("d")
            time.sleep(0.1)
            w_s()
            keyboard.press("d")

        count += 1
except KeyboardInterrupt:
    keyboard.release("d")
    exit(1)
except Exception:
    keyboard.release("d")
    exit(1)

exit(1)
