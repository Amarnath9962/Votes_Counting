Votes   = ["Boby",'Carle','Boby','Rahul','Raja','Boby','Raja','Boby','Anand','Anand','Classi','Classi','Raja',"Hero",'Rahul','Classi']
Canditate = []
votes = []

for word in Votes:
    if word not in Canditate:
        Canditate.append(word)
        votes.append(1)
    else:
        can_ind = Canditate.index(word)
        votes[can_ind]+=1
# print(Canditate)
# print(votes)

max_votes = 0

for x in range(len(votes)):
    if votes[x]>=max_votes:
        max_votes = votes[x]
        Person = []
        Person.append(Canditate[x])

print("The "+Canditate[0]+" won by "+str(max_votes)+" Votes")