"""Create a file “numbers.txt” and write the numbers 1 to 10 into the file.. """
file=open("numbers.txt","w",encoding="utf-8")  #We open a file with encoding
file.write(r"1\n")    #We write 1 to 10
file.write(r"2\n")
file.write(r"3\n")
file.write(r"4\n")
file.write(r"5\n")
file.write(r"6\n")
file.write(r"7\n")
file.write(r"8\n")
file.write(r"9\n")
file.write(r"10")
file.close()     #We have to close file