import webbrowser, time
url = input("Enter url: ")
duration = input("Enter how many views: ")

for i in range(5):
    webbrowser.open_new(url)
    time.sleep(int(duration))