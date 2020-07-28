#!/usr/bin/python
import os
import re
import sys


def replace_all_words(filename, file_re, ORIGINAL_WORD, UPDATED_WORD):
    with open(filename, "r") as f:
        f_lines = f.readlines()
        ORIGINAL_WORD_re = f"{ORIGINAL_WORD}"
        new_lines = []
        for line in f_lines:
            new_line = re.sub(ORIGINAL_WORD_re, UPDATED_WORD, line)
            new_lines.append(new_line)

    with open(filename, "w") as f:
        f.writelines(new_lines)
    return


def rep_folder(path, from_re, to_re, file_re):
    print("Current Path: {}".format(path))
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            if re.search(file_re, filename):
                infile = os.path.join(dirpath, filename)
                try:
                    replace_all_words(infile, file_re, from_re, to_re)
                except Exception as e:
                    print("! Error when reading file {} with exception {}".format(
                        infile, e))


def main():
    nums = len(sys.argv)
    if nums not in (3, 4):
        print('Usage: replacex FROM_REGEX TO_REGEX [FILENAME_REGEX]')
        exit()

    path = os.getcwd()
    ORIGINAL_WORD = sys.argv[1]
    UPDATED_WORD = sys.argv[2]
    filename_regex = r"[\w]+\.m$"

    rep_folder(path, ORIGINAL_WORD, UPDATED_WORD, filename_regex)


if __name__ == "__main__":
    main()
