file = open("manipulating_files\lorem.txt", "w")

file.write("Writing something in the file")
file.writelines(["\n""more" "\n" "thing" "\n" "written in" "\n" "the line"])
file.close()