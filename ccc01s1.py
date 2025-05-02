# Keeping Score

s=(input())
cardsMap={'A':4,'K':3,'Q':2,'J':1}

def check(suit,suitTotal):
    bonus={0:3,1:2,2:1}
    return suitTotal+bonus[len(suit)] if len(suit)<3 else suitTotal

clubs=' '.join(s[1:s.index("D")])
diamonds=' '.join(s[s.index("D")+1:s.index("H")])
hearts=' '.join(s[s.index("H")+1:s.index("S")])
spades=' '.join(s[s.index("S")+1:])

clubsTotal=sum(cardsMap[card] for card in clubs if card in cardsMap)
diamondsTotal=sum(cardsMap[card] for card in diamonds if card in cardsMap)
heartsTotal=sum(cardsMap[card] for card in hearts if card in cardsMap)
spadesTotal=sum(cardsMap[card] for card in spades if card in cardsMap)

print("Cards dealt \tPoints")
print(f'Clubs {clubs}\t{check(clubs,clubsTotal)}')
print(f'Diamonds {diamonds}\t{check(diamonds,diamondsTotal)}')
print(f'Hearts {hearts}\t{check(hearts,heartsTotal)}')
print(f'Spades {spades}\t{check(spades,spadesTotal)}')
print(f'\nTotal {check(clubs,clubsTotal)+check(diamonds,diamondsTotal)+check(hearts,heartsTotal)+check(spades,spadesTotal)}')