score = 0

print "Electric Guitar Quiz"

print "Question 1: Who pioneered the invention of the solid-body electric guitar?"
print "\tA) Jimi Hendrix\n\tB) Les Paul\n\tC) Eric Clapton\n\tD) B.B. King"

user = raw_input("")

if user == "B" or user == "b":
	score += 1

print "Question 2: What is the order of strings on a conventional electric guitar?"
print "\tA) AEDGBE\n\tB) CDEFGB\n\tC) EADGBE\n\tD) ABCDEF"

user = raw_input("")

if user == "C" or user == "c":
	score += 1

print "Question 3: Which of the following is not a brand of electric guitar?"
print "\tA) Smith\n\tB) Jackson\n\tC) Taylor\n\tD)Martin"

user = raw_input("")

if user == "A" or user == "a":
	score += 1

print score / 3
