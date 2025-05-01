# Keeping Score

s=(input())

cardsMap={'A':4,'K':3,'Q':2,'J':1}


clubs=' '.join(s[1:s.index("D")])
diamonds=' '.join(s[s.index("D")+1:s.index("H")])
hearts=' '.join(s[s.index("H")+1:s.index("S")])
spades=' '.join(s[s.index("S")+1:])


clubsTotal=sum(cardsMap[card] for card in clubs if card in cardsMap)
diamondsTotal=sum(cardsMap[card] for card in diamonds if card in cardsMap)
heartsTotal=sum(cardsMap[card] for card in hearts if card in cardsMap)
spadesTotal=sum(cardsMap[card] for card in spades if card in cardsMap)


print("Cards dealt\tPoints")
print(f'Clubs {clubs}\t{clubsTotal}')
print(f'diamonds {diamonds}\t{diamondsTotal}')
print(f'hearts {hearts}\t{heartsTotal}')