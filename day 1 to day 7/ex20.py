import time
try:
    count = 0
    while True:
        print("hello")
        count += 1
        if count == 5:
            break
        else:
            time.sleep(2)
except KeyboardInterrupt:
    print("ctrl and c pressed")
finally:
    print("always executed")


