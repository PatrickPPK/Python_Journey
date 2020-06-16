################################################################################################
# ----------------------------------------------------------------------------------------------
# Module 5 [Input-Output]
# Topic: Input-output Printing on screen, reading data from keyboard,
# opening and closing console file
# Assignment Level Basic
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# B1: What is File function in python? What is keywords to create and write file
################################################################################################
# Answer: In Python, file function is used to create, read, write and/or append real files
#         on the file system.
#         open(<filename>,<access_mode>) function is used to handle file related operations.
#         To create and to open file in write mode: f = open('filename.txt','w')

################################################################################################
# B2: Write a Python program to read an entire text file
################################################################################################
# f = open('filename.txt','r')
# print(f"File contents:\n{f.read()}")
# f.close()
#
################################################################################################
# B3: Write a Python program to append text to a file and display the text.
################################################################################################
# f = open('filename.txt','a+')
# print("----------")
# f.seek(0)
# print(f"File contents before appending to it:\n{f.read()}")
# print("----------")
# line = "I'm an append line at the end of the file filename.txt"
# f.write(line)
# f.seek(0)
# print(f"File contents after appending to it:\n{f.read()}")
# print("----------")
# f.close()
#
################################################################################################
# B4: Write a Python program to read first n lines of a file
###############################################################################################
# import random
# with open('filename.txt','r') as FileObj:
#     lines = FileObj.readlines()
#     first_n_lines = random.randrange(1,6)
#     for n in range(first_n_lines):
#         print(f"filename.txt:{n:02}: {lines[n].strip()}")
#
################################################################################################
# B5: Write a Python program to read last n lines of a file
################################################################################################
# import random
# with open('filename.txt','r') as FileObj:
#     lines = FileObj.readlines()
#     last_n_lines = random.randrange(1,6)
#     for n in range(1,last_n_lines+1):
#         print(f"filename.txt:{-n:02}: {lines[-n].strip()}")
#
################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Intermediate
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# I1: Write a Python program to read a file line by line and store it into a list
################################################################################################
# with open('filename.txt','r') as FileObj:
#     lines = []
#     for line in FileObj:
#         lines.append(line.strip())
#
################################################################################################
# I2: Write a Python program to read a file line by line store it into a variable.
################################################################################################
# with open('filename.txt','r') as FileObj:
#     lines_separated_by_newline_char = ''
#     for line in FileObj:
#         lines_separated_by_newline_char += line
#
################################################################################################
# I3: Write a python program to find the longest words
################################################################################################
# with open('filename.txt','r') as FileObj:
#     longest_word = ''
#     longest_word_length = 0
#     for line in FileObj:
#         words = (line.strip()).split()
#         for word in words:
#             if len(word) > longest_word_length:
#                 longest_word = word
#                 longest_word_length = len(word)
# print(f"Longest word in the 'filename.txt' file is: {longest_word} with length: "
#       f"{longest_word_length}")
#
################################################################################################
# I4: Write a Python program to count the number of lines in a text file.
################################################################################################
# with open('filename.txt','r') as FileObj:
#     lines = FileObj.readlines()
#     print(f"Total number of lines in file 'filename.txt' is: {len(lines)}")
#
################################################################################################
# I5: Write a Python program to count the frequency of words in a file
################################################################################################
# with open('filename.txt','r') as FileObj:
#     words_frequency_dict = {}
#     for line in FileObj:
#         words = (line.strip()).split()
#         for word in words:
#             if word in words_frequency_dict:
#                 words_frequency_dict[word] += 1
#             else:
#                 words_frequency_dict[word] = 1
# print(f"{'word':>20s} : {'frequency':>10s}")
# print(f"{'-':->20s} : {'-':->10s}")
# for key in words_frequency_dict:
#     print(f"{key:>20} : {words_frequency_dict[key]:>10}")
#
################################################################################################
# I6: Write a Python program to write a list to a file.
################################################################################################
# from string import *
# with open('filename_I6.txt','w+') as FileObj:
#     lines = [ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits]
#     for line in lines:
#         FileObj.write(line + '\n')
#     FileObj.seek(0)
#     print("----------")
#     print(f"File contents after writing to it")
#     print("----------")
#     print(f"{FileObj.read()}")
#     print("----------")

################################################################################################
# I7: Write a Python program to copy the contents of a file to another file
################################################################################################
# with open('filename.txt','r') as ReadObj:
#     with open('filename_I7.txt','w') as WriteObj:
#         for line in ReadObj:
#             WriteObj.write(line)

################################################################################################
# ----------------------------------------------------------------------------------------------
# Assignment Level Advance
# ----------------------------------------------------------------------------------------------
################################################################################################

################################################################################################
# A1: Write a Python program to read a random line from a file
################################################################################################
# import random
# with open('filename.txt','r') as FileObj:
#     lines = FileObj.readlines()
#     line_no = random.randrange(0,6)
#     print(f"filename.txt:{line_no:02}: {lines[line_no].strip()}")
#
################################################################################################
# A2: Write a Python program to assess if a file is closed or not
################################################################################################
# with open('filename.txt','r') as FileObj:
#     print(f"In with clause: status of Fileobj.closed: {FileObj.closed}")
# print(f"After with clause: status of Fileobj.closed: {FileObj.closed}")
#
################################################################################################
# A3: Write a Python program to remove newline characters from a file.
################################################################################################
# with open('filename.txt','r+') as FileObj:
#     lines = FileObj.readlines()
#     FileObj.seek(0)
#     for line in lines:
#         FileObj.write(line.replace('\n',''))

