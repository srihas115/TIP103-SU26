def can_trust_message(message):
    #alpha_set = set(chr(i) for i in range(97, 123))
    alpha_set = set()
    for c in message:
        if c != ' ':
            alpha_set.add(c.lower())

    return len(alpha_set) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))