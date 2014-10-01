# scrape for all the pages

import requests
import re

template = "http://www.ratemyprofessors.com/search.jsp?query=university+of+miami&offset="
holder = []
pattern = re.compile("\/ShowRatings\.jsp\?tid=(\d+)")

with open("ids.txt", "r+") as writeIds:
	for i in xrange(0,104):
		r = requests.get(template + str(i*20))
		matches = pattern.findall(r.text)
		for m in matches:
			num = int(m)
			holder.append(num)
			writeIds.write(str(num) + "\n")
		print(matches)
		print("~~~" + str(len(holder)) + "~~~")