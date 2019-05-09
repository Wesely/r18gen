# coding=UTF-8
import re
import os
import errno

# ignore the first IGNORE_COL_NUM column, the 3rd and after columns are considered to be content of r18n.
IGNORE_COL_NUM = 2 

# The TSV file export from GoogleDrive's SpreadSheet
FILENAME = "strings_r18n.tsv"

# Generate Android XML
GENERATE_ANDROID = True # not used yet

# Android format
ANDROID_CONTENT = '\t<string name="{}">{}</string>'
ANDROID_COMMENT = "<!-- {} -->"
ANDROID_FILENAME = "output/android/values-{}/strings.xml"

def write_content(content,android_files):
    group = ''
    for x in content:
        line = re.split('\t',x.replace('\r','').replace('\n',''))
        first = str(line.pop(0))
        if len(first) > 0: 
            group = first
            print('- Group : '+ group)
            for f in android_files:
                # write format
                f.write(ANDROID_COMMENT.format(group) + "\n")
        name = line.pop(0)
        if len(line) != len(android_files):
            print("length inconsistent")
            pass
        for index, entry in enumerate(line):
            print ("-- " + name + " : " +entry)
            # write format
            android_files[index].write(ANDROID_CONTENT.format(group + "_" + name, entry) + "\n")
 
if __name__ == "__main__":
    f = open(FILENAME, "r")
    head = re.split('\t', f.readline().replace('\r','').replace('\n',''))
    for i in range(IGNORE_COL_NUM):
        head.pop(0)
    android_files = [] # list
    for lang in head:
        file_path = ANDROID_FILENAME.format(str(lang))
        if not os.path.exists(os.path.dirname(file_path)):
            try:
                os.makedirs(os.path.dirname(file_path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        f_lang = open(file_path, "w")
        f_lang.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n')
        android_files.append(f_lang)

    content = f
    print(head)
    write_content(content,android_files)
    f.close()
    for f in android_files:
        f.write('</resources>')
        f.close()
    pass
