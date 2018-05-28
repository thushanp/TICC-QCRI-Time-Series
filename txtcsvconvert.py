import csv

num = 112


blob = []
for i in xrange(0,112):
	curline = [float(x) for x in (raw_input().split())]
	blob.append(curline)

print(blob)
with open('myres.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in blob:
		spamwriter.writerow(i)