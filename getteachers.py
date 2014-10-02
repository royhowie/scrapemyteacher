#get all the teachers
import requests
import re

tLink = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid="

name = re.compile('class="p.name">(.+)</span>')
overall = re.compile('Overall Quality\s+.+>(.+)</div')
average = re.compile('Average Grade\s+.+>(.+)</div')

labels = re.compile('"label">(.+)</div>')
grades = re.compile('"rating">(.+)</div>')

counter = 0

with open("data.txt", "r+") as writeHere:
	writeHere.write("name,overall,average,helpfulness,clarity,easiness,reviews,\n")
	with open("ids.txt", "r") as getNumbers:
		lines = getNumbers.read().split("\n")
		for l in lines:
			counter += 1

			r = requests.get(tLink + l).text.split("<!-- Professor info -->")[1].split("<!-- Ends Rating Column -->")[0]

			names = name.findall(r)
			overallQuality = overall.findall(r)
			averageGrade = average.findall(r)
			l = labels.findall(r)
			g = grades.findall(r)

			data = (names[0] + " " + names[1]).strip().encode("utf8") + "," + overallQuality[0].encode("utf8") + "," + averageGrade[0].encode("utf8") + ","
			for singleGrade in g:
				data += (singleGrade.encode("utf8") + ",")

			writeHere.write(data + "\n")

			print("on professor #" + str(counter) + " " + (names[0] + " " + names[1]).strip().encode("utf8"))