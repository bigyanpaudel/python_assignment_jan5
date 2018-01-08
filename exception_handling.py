def main():
    try:
        fh=open('lines.txt')
    except IOError as e:
        print("couldnot open te file:",e)
    else:
        for line in fh:print(line.strip())
    finally:
        print("create a file")
main()