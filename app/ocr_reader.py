import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext("../menu.jpg", detail=0)

for line in result:
    print(line)