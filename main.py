# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def ocr(img):
    import easyocr
    reader = easyocr.Reader(['ch_sim', 'en'])  # need to run only once to load model into memory
    result = reader.readtext(img, detail=0)
    for row in result:
        print(row)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ocr('python.jpg')
