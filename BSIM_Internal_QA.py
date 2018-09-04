#!/usr/bin/env python3.6

import os # For file listing
import re # Regular expression
import time # Timer

def main_menu():
    print("""--------------------------------
Software: BSIM Internal QA Program
Author: Dr. Huan-Lin Chang, UC Berkeley
Updated: 9/3/2018
Email: huanlinberkeley@gmail.com
--------------------------------
Program Menu:
[1] Check divide-by-zeros
[2] Check square roots
[3] Check logarithm
[4] Check exponential
[Q] Leave program""")
    return None

def _list_files():
    return([
        file
        for file in os.listdir('./code')
        if file.endswith(".include") or file.endswith(".va")
    ])

def _search_param(_all_files):
    re_par = re.compile(r"(^`MPRnb)|(^`IPRnb)|(^`MPRcz)|(^`IPRcz)") # Open file and search for MPRnb, IPRnb, MPRcz, and IPRcz parameters
    re_word = re.compile(r"\W+") # Split line by words
    _param = []
    for file in _all_files:
        with open('./code/' + file, "r", encoding="utf8") as f:
            f_par = [
                re_word.split(line)[2] # Split the line and extract parameters into a list
                for line in f
                if re_par.search(line)
            ]
        _param += f_par
    return(_param)

def _search_line(_all_files, _param):
    re_comment = re.compile(r"\s*\/{2}.*") # Find comment line
    re_block = re.compile(r"\s*\/\*.*") # Find block comment lines
    print(f"----------------------------------")
    print(f"Now writing into file 'check_divide_by_zero.txt'...... ")
    start_time = time.time()
    # Open file to search for divide-by-zero cases
    with open("check_divide_by_zero.txt", "w") as fout:
        for file in _all_files:
            fout.write(f"In file {file}:\n")
            for i in _param:
                item = r"\/{1}\s*\(*(\b" + i + r"\b)"
                re_tar = re.compile(item)
                with open('./code/' + file, "r", encoding="utf8") as fin:
                    count = 0
                    catch = []
                    for num, line in enumerate(fin, start=1):
                        if re_tar.search(line) and not re_comment.search(line) and not re_block.search(line) and not re.search(r"^`", line):
                            count += 1
                            catch.append("Line " + str(num) + " " + line)
                    if count > 0:
                        fout.write(f"{' '*4}Found {count} possible divide-by-zero cases of {i}: \n")
                        for j in catch:
                            fout.write(f"{' '*8}{j}")
    stop_time = time.time()
    print(f"Done! It takes {round(stop_time - start_time, 1)} seconds!")
    with open("check_divide_by_zero.txt", "r") as f:
        for line in f:
            print(line, end="")
    return None

def divide_by_zero():
    _all_files = _list_files()
    _param = _search_param(_all_files)
    _search_line(_all_files, _param)
    return None

def square_root():
    _all_files = _list_files()
    re_comment = re.compile(r"\s*\/{2}.*") # Find comment line
    re_block = re.compile(r"\s*\/\*.*") # Find block comment lines
    re_sqrt = re.compile(r"(sqrt\()") # Find sqrt
    print(f"----------------------------------")
    print(f"Now writing into file 'check_square_roots.txt'...... ")
    start_time = time.time()
    # Open file to search for sqrt() cases
    with open("check_square_roots.txt", "w") as fout:
        for file in _all_files:
            fout.write(f"In file {file}:\n")
            with open('./code/' + file, "r", encoding="utf8") as fin:
                count = 0
                catch = []
                for num, line in enumerate(fin, start=1):
                    if re_sqrt.search(line) and not re_comment.search(line) and not re_block.search(line):
                        count += 1
                        catch.append("Line " + str(num) + " " + line)
                if count > 0:
                    fout.write(f"{' '*4}Found {count} square root cases\n")
                    for j in catch:
                        fout.write(f"{' '*8}{j}")
    stop_time = time.time()
    print(f"Done! It takes {round(stop_time - start_time, 1)} seconds!")
    with open("check_square_roots.txt", "r") as f:
        for line in f:
            print(line, end="")
    return None

def logarithm():
    _all_files = _list_files()
    re_comment = re.compile(r"\s*\/{2}.*") # Find comment line
    re_block = re.compile(r"\s*\/\*.*") # Find block comment lines
    re_log = re.compile(r"(?<!l)(ln\()(?!x)") # Find ln, not lln
    print(f"----------------------------------")
    print(f"Now writing into file 'check_logarithm.txt'...... ")
    start_time = time.time()
    # Open file to search for sqrt() cases
    with open("check_logarithm.txt", "w") as fout:
        for file in _all_files:
            fout.write(f"In file {file}:\n")
            with open('./code/' + file, "r", encoding="utf8") as fin:
                count = 0
                catch = []
                for num, line in enumerate(fin, start=1):
                    if re_log.search(line) and not re_comment.search(line) and not re_block.search(line):
                        count += 1
                        catch.append("Line " + str(num) + " " + line)
                if count > 0:
                    fout.write(f"{' '*4}Found {count} logarithm cases\n")
                    for j in catch:
                        fout.write(f"{' '*8}{j}")
    stop_time = time.time()
    print(f"Done! It takes {round(stop_time - start_time, 1)} seconds!")
    with open("check_logarithm.txt", "r") as f:
        for line in f:
            print(line, end="")
    return None

def exponential():
    _all_files = _list_files()
    re_comment = re.compile(r"\s*\/{2}.*") # Find comment line
    re_block = re.compile(r"\s*\/\*.*") # Find block comment lines
    re_exp = re.compile(r"(?<!l)(exp\()(?!x)") # Find exp, not lexp
    print(f"----------------------------------")
    print(f"Now writing into file 'check_exponential.txt'...... ")
    start_time = time.time()
    # Open file to search for exp() cases
    with open("check_exponential.txt", "w") as fout:
        for file in _all_files:
            fout.write(f"In file {file}:\n")
            with open('./code/' + file, "r", encoding="utf8") as fin:
                count = 0
                catch = []
                for num, line in enumerate(fin, start=1):
                    if re_exp.search(line) and not re_comment.search(line) and not re_block.search(line):
                        count += 1
                        catch.append("Line " + str(num) + " " + line)
                if count > 0:
                    fout.write(f"{' '*4}Found {count} exponential cases\n")
                    for j in catch:
                        fout.write(f"{' '*8}{j}")
    stop_time = time.time()
    print(f"Done! It takes {round(stop_time - start_time, 1)} seconds!")
    with open("check_exponential.txt", "r") as f:
        for line in f:
            print(line, end="")
    return None

def main():
    main_menu()
    sel = '0'
    while sel != 'Q':
        sel = input("Please choose an option (Enter a number or Q to leave): ")
        if sel == '1':
            divide_by_zero()
            break
        if sel == '2':
            square_root()
            break
        if sel == '3':
            logarithm()
            break
        if sel == '4':
            exponential()
            break
    return None

if __name__ == "__main__":
    main()
