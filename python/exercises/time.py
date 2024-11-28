def timee():
    import time
    hour=time.strftime('%H:%M:%S')
    print()
    print('to know time press enter')
    input()
    print(hour)
    timee()
timee()
