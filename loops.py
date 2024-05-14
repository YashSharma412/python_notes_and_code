# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ["John", "Corey", "Adam", "Steve", "Rick", "Stefan"]

def runLoop():
    for person in people:
        print(f"Current Person: {person}")


# ! Break out
def runLoopBreak():
    for person in people:
        if(person == "Steve"):
            break
        print(f"Current Person: {person}")

def runLoopContinue():
    for person in people:
        if(person == "Steve"):
            continue
        print(f"Current Person: {person}")
# runLoop()
# runLoopBreak()
runLoopContinue()

# While loops execute a set of statements as long as a condition is true.
