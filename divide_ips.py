import sys

# read the input file name from the command-line arguments
file_name = sys.argv[1]

# read the input file and create a list of IP addresses
with open(file_name, 'r') as f:
    ips = f.read().split('\n')

# divide the list of IPs into sub-lists of 10 IPs each
for i in range(0, len(ips), 10):
    sub_list = ips[i:i+10]
    
    # write the sub-list to a different file
    with open('ips_{}.txt'.format(i), 'w') as f:
        f.write('\n'.join(sub_list))
