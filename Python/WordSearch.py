line = 1
word = "Python".lower()
with open("sample.txt", "r") as f:
    while True:
        data = f.readline().lower()
        if(word in data):
            print(f"{word} found at line {line}")
            break
        line += 1
        
        if data == "":
            print(f"{word} not found in the file")
            break