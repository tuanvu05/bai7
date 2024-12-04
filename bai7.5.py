def file_read(fname):
    with open(fname, "w", encoding='utf-8') as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    with open(fname, "r", encoding='utf-8') as txt:
        print(txt.read())
file_read('abc.txt')
