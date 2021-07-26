import webbrowser

url = "https://www.python.org/"
try:
    wb = webbrowser.open(url, new=0, autoraise=True)
    print(f"Successfully Executed - Status:{wb}")
except Exception as e:
    print(e)
    print(f"An Error Ocurred - Status:{wb}")

# opening url in new tab everytime
new_tab = webbrowser.open_new(url)
print(f"Successfully Executed: {new_tab}")
