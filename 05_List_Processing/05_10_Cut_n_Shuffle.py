cards = input().split()
modes = list(input())

number_of_cards = len(cards)

for m in modes:
    if m == 'C':
        for i in range(int(number_of_cards/2)):
            cards.append(cards[0])
            del cards[0]
    elif m == 'S':
        left = []
        for i in range(int(number_of_cards/2)):
            left.append(cards[0])
            del cards[0]
        right = cards
        left_index = 1
        right_index = 0       

        while len(right) != 0:
            left.insert(left_index,right[0])
            left_index += 2
            del right[0]
        cards = left
    else:
        pass

result = ""

for card in cards:
    result += card
    result += " "

print(result.strip())