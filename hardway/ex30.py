people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

########################################
if people < cars and buses > cars:
    print "We can take buses."
elif people < cars and buses < cars:
    print "We take cars."
else:
    print "We stay home."

if people < buses and buses > cars:
    print "We take buses."
elif people < buses and buses < cars:
    print "We take cars."
elif people > buses and people < cars:
    print "We take cars."
else:
    print "We stay home."
