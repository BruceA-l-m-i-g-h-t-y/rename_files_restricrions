
import os

if __name__ == '__main__':

    folder_path = "C:/some_folder"
    wanted_chars = ["א","1", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ", "ך", "ל",
                    "מ", "ם", "נ", "ן", "ס", "ע", "פ", "ף", "צ", "ץ", "ק", "ר", "ש",
                    "ת", "ם", "ך", "ן","-",".","m",",M","k","K","V","v"," "]
    unwanted_strings = ["aaa",
                        "bbb",
                        "ccc"]

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a file (not a folder)
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Remove unwanted characters from the filename
            new_filename = ''.join(c for c in filename if c in wanted_chars)
            # Remove unwanted strings from the filename
            for s in unwanted_strings:
                new_filename = new_filename.replace(s, "")

            # clear space character at the begining and at the end of the filename
            new_filename = new_filename.lstrip()
            basename, ext = os.path.splitext(new_filename)
            basename = basename.rstrip()
            new_filename = basename + ext
            # Rename the file
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)


