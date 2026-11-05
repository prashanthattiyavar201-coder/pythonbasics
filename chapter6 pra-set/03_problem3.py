p1 = "Make lot of money"
p2 = "Buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter you messaag: ")

if(p1 in message)or(p2 in message)or(p3 in message)or(p4 in message):
    print("This commet is spam")
else:
    print("This comment is not spam")    