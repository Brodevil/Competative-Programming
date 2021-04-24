# Python practise 15 - (Question from codewithharry) - Clear the clutter
# Actaully we will work with file in clear the clutter folder which will be not avaiable in the, we had ignore it. AS we will working with fwe files and also to keep everython organized we had created that folder 
# and inside that folder a main.py will going to handle everything, the file contain mp3 and mp4 file which can make a issue. So we ignore that directory
# But the mine.py code will also availabe here bro


"""
Clear the clutter :

Make a python program that will sort everything i.e. Clearing the clutter of a specific folder 
It suppose to created the folder on the name of the specefic extension 
And the file will be inside its entention name file 

Note : Use os module and the work is in the cler the clutter directory in Abhinav's computer not on github as it had ignore due to some uage data containing files too

Example:

A file containing :
love dose.mp3
love dose.mp4
youyou.mp3
main.py
__init__.py
__main__.py
index.html
.
.
.
Such many file

So now the files will be created MP3, MP4, PY, HTML, etc. and those folder will be containing the there name extension of the file

Extra problem : 
    This is a extra problem that Abhinav had made by his own that If afterwards also the directory will get full of all clutter and after running that
    python program the file will be go inside in the folder if avaiable other wise a new extension will get inside a new folder as per its extension name
    So, All the best to me
"""

# Author = Abhinav
# Date = 23 April 2021
# Motive = Just for the python practise to not just learn python also to expert it

import os


def clearClutter(path):
    """This functions is hardCore of the program as it will clear clutter the whole directory while it just created the folder on the name of its extension"""
    files = os.listdir(path)
    extension = set()
    for file in files:
        if os.path.isfile(file):
            extension.add(file.split(".")[1])

    for folder in extension:
        if not os.path.exists(f"{os.path.join(path, folder.capitalize())}"):
            os.mkdir(f"{os.path.join(path, folder.capitalize())}")
        for file in files:
            os.replace(os.path.join(path, file), f"{os.path.join(path, folder.capitalize(), file)}")
            


def isPathExistsToMakeFile(path):
    """Checking that a file or a path is exiting or not if not that it will be created """
    if not os.path.exists(path):
        os.mkdir(path)


def clearClutter2(path):
    """This is the 2nd function that will just created Media, Images and Docs file and additionally I will make seperate code for few selected extensions"""
    isPathExistsToMakeFile("Images")
    isPathExistsToMakeFile("Docs")
    isPathExistsToMakeFile("Media")
    isPathExistsToMakeFile("Code")
    isPathExistsToMakeFile("UnKnownFiles")


    images = ["Images",".jpg", ".png", ".jpeg", ".gif"]
    code = ["Code", ".py", ".c", ".cpp", ".htm", ".html", ".json", ".xml", '.gitignore', ".md", ".pyc", ".bat", ".java", ".r", ".env", "LICENSE"]
    media = ["Media", ".mp3", ".mp4"]
    docs = ["Docs", ".pptx", ".dot", ".docx", ".pdf", ".docm", ".dotx", ".rtf", ".txt", ".wps", ".xps", ".csv", ".xlsx", ".xlsm", ".xlsb", ".xltx", ".xltm", ".xls", ".xlt", ".xlam", ".xla", ".xlw", ".xlr"]
    typeFile = [images, code, media, docs]

    files = os.listdir(path)
    for file in files:
        if file != "main.py":
            if os.path.isfile(file):
                print(file)
                for i in typeFile:
                    print(i)
                    print(os.path.splitext(file)[1])
                    if os.path.splitext(file)[1] in i:
                        print("Condition satisfied")
                        os.replace(os.path.join(path, file), os.path.join(path, i[0], file))
                        break

                try:
                    os.replace(os.path.join(path, file), os.path.join(path, "UnknownFiles", file))
                except Exception as a:
                    print("Condition not satisfied")
                    print(a)


if __name__ == "__main__":
    os.chdir(r"C:\Users\ADMIN\PycharmProjects\Practice Python\Clear The Clutter")
    # clearClutter(os.getcwd()) 
    clearClutter2(os.getcwd())

