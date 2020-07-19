
numBottles = 2
numExchange = 3

EmptyBottle = numBottles
TotalBottle = numBottles

while EmptyBottle >= numExchange:

    TotalBottle += (numBottles // numExchange)
    EmptyBottle = numBottles // numExchange + numBottles % numExchange
    numBottles = EmptyBottle

print(TotalBottle)