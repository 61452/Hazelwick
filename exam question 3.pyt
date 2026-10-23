A=0
B=0
C=0
vote = ""
while vote != "END" and vote != "end":
    vote = input("Enter your vote (A, B, C) or 'END' to finish: ")
    if vote == "A" or vote == "a":
        A += 1
    elif vote == "B" or vote == "b":
        B += 1
    elif vote == "C" or vote == "c":
        C += 1
    else:
        print("Invalid vote. Please enter A, B, C, or 'END' to finish.")

print(f"Votes for A: {A}")
print(f"Votes for B: {B}")
print(f"Votes for C: {C}")
print(f"Total votes: {A + B + C}")