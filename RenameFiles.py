# Rename Files 1.1
# By Arnob Paul
# https://arnobpl.github.io
# arnobpl@gmail.com


import os

from NumerizeFiles import version, input_directory_path, listdir_no_hidden

if __name__ == "__main__":
    print("Rename Files " + version + "\nDeveloped by Arnob Paul\nhttps://arnobpl.github.io\n" +
          "WARNING: Although preview and confirmation prompt are given," +
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
        string = input("Enter command to rename the files (eg \"filename[:]\"):\n")
        i = 1
        print("\nPreview:")
        confirm = ""
        try:
            for filename in file_list_from_input:
                originalPreview = filename
                if len(originalPreview) > 29:
                    originalPreview = originalPreview[:27]
                    originalPreview += "..."
                else:
                    originalPreview += "\""
                renamedPreview = eval(string, {"filename": filename, "__builtins__": {}}, {})
                if len(renamedPreview) > 29:
                    renamedPreview = renamedPreview[:27]
                    renamedPreview += "..."
                else:
                    renamedPreview += "\""
                print("{:03}.   ".format(i) + "{:>31}".format("\"" + originalPreview) + "   -->   " + "{:31}".format(
                    "\"" + renamedPreview))
                i += 1
            if i == 1:
                input("<empty>\nNo files to rename.\nPress Enter to exit...")
            else:
                confirm = input("\nAre you sure to rename the files like above these? (y/n):\n").strip().lower()
                if confirm == "y":
                    print("Please wait...\n")
                    for filename in file_list_from_input:
                        os.rename(os.path.join(input_path, filename),
                                  os.path.join(input_path,
                                               eval(string, {"filename": filename, "__builtins__": {}}, {})))
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
