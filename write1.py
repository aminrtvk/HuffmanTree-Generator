import sys
import os

if len(sys.argv) != 3:
    sys.exit("Invalid arguments!")

in_file = sys.argv[1]
out_file = sys.argv[2]

if os.path.exists(in_file) is False:
    sys.exit("Input file does not exist!")
domains = []
in_file_handler = open(in_file)
out_file_handler = open(out_file, "w")
for line in in_file_handler:
    domain = line.rstrip.split("@")
    domains.append(domain[1])
dictionary_count_name = {}
for i in len(domains):
    l = 1
    if domain[i] == domain[i+1]:
        dictionary_count_name[domain[i+1]]= l + 1
    else:
        dictionary_count_name[domain[i]]= l
for keys , count in dictionary_count_name.items():
    out_file_handler.write(f"{key}"+f"{value}\n")
in_file_handler.close()
out_file_handler.close()





