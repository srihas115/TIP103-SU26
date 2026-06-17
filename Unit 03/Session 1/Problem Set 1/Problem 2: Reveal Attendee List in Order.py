def reveal_attendee_list_in_order(attendees):
    # possibly use a deque 
    # SORT ATTENDEES FIRST INCREASINGLY
    # attendees = [17,13,11,2,3,5,7]
    # sorted_attendees = [2,3,5,7,11,13,17]
    


# -----------
    # dq = [0,1,2,3,4,5,6]
    # sorted = [2,3,5,7,11,13,17]
    
    # dq = [2,3,4,5,6,1]
    # result = [0]

    # dq = [4,5,6,1,3]
    # result = [0,2]

    # dq = [6,1,3,5]
    # result = [0,2,4]

    # dq = [3,5,1]
    # result = [0,2,4,6]

    # dq = [1,5]
    # result = [0,2,4,6,3]

    # dq = [5]
    # result = [0,2,4,6,3,1]

    # dq = []
    # result = [0,2,4,6,3,1,5]
    # sorted = [2,3,5,7,11,13,17]
    # [2,13,3,11,5,17,7]



    # attendees.sort()

    # result = [0] * len(attendees)
    # while dq:


    # pass


print(reveal_attendee_list_in_order([17,13,11,2,3,5,7]))
print(reveal_attendee_list_in_order([1,1000]))