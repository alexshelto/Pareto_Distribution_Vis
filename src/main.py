
import random 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


'''
unique individuals: 1000 of them
each individual has 10$ to start

each iteration, select 2 random individuals who have >= $1
    -> Coin flip decides who takes a dollar from the other person 

graph the number of people with each dollar amount 


'''



class Individual:
    def __init__(self, money):
        self.money = money



out_of_money = 0 #number of individuals who hit $0
with_money = [Individual(10) for x in range(20000)]



# x count: dollars 0-60
# y count: how many people have each amount of dollars for index x of x_count

def trading(i):
    global out_of_money

    for i in range(200): 
        looser = None
        trader0 = random.randint(0, len(with_money)-1)
        trader1 = random.randint(0, len(with_money)-1)

        # if 1, trader 1 wins $1 else trader 0
        coinflip = random.randint(0,1)
        if coinflip == 1:
            with_money[trader0].money += 1
            with_money[trader1].money -= 1
            looser = trader1
        else:
            with_money[trader0].money -= 1
            with_money[trader1].money += 1
            looser = trader0

        if with_money[looser].money == 0:
            del with_money[looser]
            out_of_money += 1

    count = {}
    '''
    for i in range(0, 60):
        count[i] = 60
    '''

    for i in with_money:
        try:
            count[i.money] += 1
        except KeyError:
            count[i.money] = 1
    count[0] = out_of_money


    plt.cla()

    plt.bar(*zip(*count.items()))

    plt.xlabel("Money Dollars")
    plt.ylabel("Individuals")




def main() -> int: 
    
    ani = FuncAnimation(plt.gcf(), trading, interval=100)
    plt.show()
    

    return 0




if __name__ == '__main__':
    exit(main())

