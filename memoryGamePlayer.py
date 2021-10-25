
cards = Pattern("cards.png")
cardsforFlipping = Pattern("cards2.png").similar(0.24)

winScreen = "winScreen.png"

cardLocations = {
        "0":  {
            "x" : -314,
            "y" : -89        
        },
        "1":  {
            "x" : -164,
            "y" : -84          
        },
        "2":  {
            "x" : 4,
            "y" : -103         
        },
        "3":  {
            "x" : 159,
            "y" : -93        
        },
        "4":  {
            "x" : 314,
            "y" : -93         
        },
        "5":  {
            "x" : -324,
            "y" : 98           
        },
        "6":  {
            "x" : -164,
            "y" : 84           
        },
        "7":  {
            "x" : 0,
            "y" : 93          
        },
        "8":  {
            "x" : 150,
            "y" : 93         
        },
        "9":  {
            "x" : 324,
            "y" : 84           
        }
}

foundCardsTypeArray = []
cardType = ["a","b","c","d","e"]
cardPairs = []
def assignCardType():
    if exists("1634243925897.png",1):
        foundCardsTypeArray.append("a")
    elif exists("1634243942839.png",1):
        foundCardsTypeArray.append("b")
    elif exists("1634243962573.png",1):
        foundCardsTypeArray.append("c")
    elif exists("1634243984017.png",1):
        foundCardsTypeArray.append("d")
    elif exists("1634243999474.png",1):
        foundCardsTypeArray.append("e")
        

for x in range(10):
    click(cards.targetOffset(cardLocations[str(x)]["x"], cardLocations[str(x)]["y"]))
    assignCardType()
    click(cards.targetOffset(cardLocations[str(x)]["x"], cardLocations[str(x)]["y"]))



for y in range(len((cardType))):
    for x in range(len(foundCardsTypeArray)):
        if foundCardsTypeArray[x] == cardType[y]:
            cardPairs.append(x)
        else: 
            pass

for x in range(10):
    click(cardsforFlipping.targetOffset(cardLocations[str(cardPairs[x])]["x"], cardLocations[str(cardPairs[x])]["y"]))
    sleep(1)

popup(find(winScreen).text().lstrip(":"))






