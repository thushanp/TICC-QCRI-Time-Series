import csv

num = 112


blob = []
for i in xrange(0,1437):
	curline = [float(x) for x in (raw_input().split())]
	# curline.reverse()
	blob.append(curline)

# blob = sorted(blob)

print(blob)
with open('freq2sort.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in blob:
		spamwriter.writerow(i)