def PvZ(zombies:list, plants:list)->bool:
    winzombies = winplants = 0
    if len(zombies)==len(plants):
        for z, p in zip(zombies, plants):
            if z<p:
                winplants+=1
            elif z>p:
                winzombies+=1
            else: 
                continue
    else:
        if len(zombies)>len(plants):
            for i in range(len(plants)):
                if zombies[i]<plants[i]:
                    winplants+=1
                elif zombies[i]>plants[i]:
                    winzombies+=1
                else: 
                    continue
            winzombies+=len(zombies)-len(plants)
        elif len(zombies)<len(plants):
            for i in range(len(zombies)):
                if zombies[i]<plants[i]:
                    winplants+=1
                elif zombies[i]>plants[i]:
                    winzombies+=1
                else: 
                    continue
            winzombies+=len(plants)-len(zombies)

    if winplants==winzombies:
        return sum(plants)>=sum(zombies)
    else:
        return winplants>winzombies


if __name__=="__main__":
   print(PvZ([ 1, 3, 5, 7 ], [ 2, 4, 6, 8 ]))
   print(PvZ([ 1, 3, 5, 7 ],[ 2, 4 ]))
   print(PvZ([ 1, 3, 5, 7 ], [ 2, 4, 0, 8 ]))
   print(PvZ([ 2, 1, 1, 1 ], [ 1, 2, 1, 1 ]))