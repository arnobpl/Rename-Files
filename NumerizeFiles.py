# Numerize Files 1.1
# By Arnob Paul
# https://arnobpl.github.io
# arnobpl@gmail.com


import os
import sys

version = "1.1"

excluded_files = ["NumerizeFiles.py", "RenameFiles.py"]

if sys.platform == "win32":  # windows
    excluded_files.append("desktop.ini")
elif sys.platform == "darwin":  # mac
    excluded_files.append(".DS_Store")


def input_directory_path():
    input_dir = input("Enter the folder path (keep empty for the current folder):\n")
    if input_dir == "" or not os.path.isabs(input_dir):
        input_dir = os.path.join(sys.path[0], input_dir)
    return input_dir


def listdir_no_hidden(path):
    file_list = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            flag = 1
            if file.startswith('.'):
                flag = 0
            else:
                for x in excluded_files:
                    if x == file:
                        flag = 0
                        break
            if flag:
                file_list.append(file)
    return file_list


if __name__ == "__main__":
    print("Numerize Files " + version + "\nDeveloped by Arnob Paul\nhttps://arnobpl.github.io\n" +
          "WARNING: Although preview and confirmation prompt are given,\n" +
          "this program can automatically rename many files at once. Be careful!\n\n")

    input_path = input_directory_path()

    file_list_from_input = []

    NO_ERROR = True
    try:
        file_list_from_input = listdir_no_hidden(input_path)
    except Exception as exception:
        NO_ERROR = False
        print(exception)
        input("Folder path is not correct. Try again.\nPress Enter to exit...")

    if NO_ERROR:
        initial_num = 1
        incrementNum = 1
        widthNum = 0

        try:
            initial_num = int(input("\nEnter beginning number (eg \"1\" to rename the first file as \"1\")\n"))
        except:
            print("Input is not a number! Default value (" + str(initial_num) + ") is taken as beginning number.\n")
        try:
            incrementNum = int(input("\nEnter incremental number (eg \"1\" to increment file name's number by 1)\n"))
        except:
            print("Input is not a number! Default value (" + str(incrementNum) + ") is taken as incremental number.\n")
        try:
            widthNum = int(input("\nEnter width (eg \"3\" to rename files like \"001\"; \"0\" for no restriction)\n"))
        except:
            print("Input is not a number! Default value (" + str(widthNum) + ") is taken as width.\n")

        begin_command = input("\nEnter command for beginning text (eg \"filename[:-4]\"; this may be empty)\n")
        if begin_command == "":
            begin_command = "\"\""

        end_command = input("\nEnter command for ending text (eg \"filename[-4:]\"; this may be empty)\n")
        if end_command == "":
            end_command = "\"\""

        i = 1
        print("\nPreview:")
        confirm = ""
        try:
            num = initial_num
            for filename in file_list_from_input:
                originalPreview = filename
                if len(originalPreview) > 29:
                    originalPreview = originalPreview[:27]
                    originalPreview += "..."
                else:
                    originalPreview += "\""
                renamedPreview = (eval(begin_command, {"filename": filename, "__builtins__": {}}, {}) +
                                  str(num).zfill(widthNum) +
                                  eval(end_command, {"filename": filename, "__builtins__": {}}, {}))
                if len(renamedPreview) > 29:
                    renamedPreview = renamedPreview[:27]
                    renamedPreview += "..."
                else:
                    renamedPreview += "\""
                print("{:03}.   ".format(i) + "{:>31}".format("\"" + originalPreview) + "   -->   " + "{:31}".format(
                    "\"" + renamedPreview))
                num += incrementNum
                i += 1
            if i == 1:
                input("<empty>\nNo files to rename.\nPress Enter to exit...")
            else:
                confirm = input("\nAre you sure to rename the files like above these? (y/n):\n").strip().lower()
                if confirm == "y":
                    print("Please wait...\n")
                    num = initial_num
                    for filename in file_list_from_input:
                        os.rename(os.path.join(input_path, filename),
                                  os.path.join(input_path,
                                               eval(begin_command, {"filename": filename, "__builtins__": {}}, {}) +
                                               str(num).zfill(widthNum) +
                                               eval(end_command, {"filename": filename, "__builtins__": {}}, {})))
                        num += incrementNum
                        print(filename[:78])
                    input("\nFiles are successfully renamed.\nPress Enter to exit...")
                else:
                    input("\nFiles are not renamed.\nPress Enter to exit...")
        except Exception as exception:
            print(exception)
            if confirm == "y":
                input("Error in operation. Try again.\nPress Enter to exit...")
            else:
                input("Command is not correct. Try again.\nPress Enter to exit...")
