# Current Points: 142 -> XXXXX

def tickets(people):
    print(f"people: {people}")
    if len(people) == 1 and people[0] == 25: return "YES"
    if len(people) > 1 and people[0] != 25: return "NO"

    change = []
    for i, v in enumerate(people):
        person = people[i]
        person_change = person - 25
        print(f"person: {person} - person_change: {person_change} ")

        if person_change == 0:
            change.append(person)
            print(f"change: {change}")
            continue
        else:

            if person_change in change:
                change.remove(person_change)
                print(f"remove change: {change}")
                continue

            return "NO"
    return "YES"