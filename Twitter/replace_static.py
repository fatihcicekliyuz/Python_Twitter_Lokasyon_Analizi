ans = 'href="'
ans2 = 'src="'

lines = []

import re

with open(r'food-index.html', mode='r') as f:
    for line in f.readlines():  # iterate thru the lines
        if ans in line: # check if is in ans in line
            m = re.search('href="(.*?)\"',line)
            ax = m.group(0)
            if "http" not in ax:
                data = ax.replace('href="',"").replace('"',"")

                line = line.replace(ax, '''href="{% static 'x' %}"'''.replace("x",data))
                print(line)
        if ans2 in line:  # check if is in ans in line
            m = re.search('src="(.*?)"', line)
            ax = m.group(0)
            if "http" not in ax:
                data = ax.replace('src="', "").replace('"', "")

                line = line.replace(ax, '''src="{% static 'x' %}"'''.replace("x", data))
                print(line)

        lines.append(line)

# write to a new file
with open(r'myfile.html', mode='w') as new_f:
    new_f.writelines(lines)
