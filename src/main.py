
import random 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation





# x count: dollars 0-60
# y count: how many people have each amount of dollars for index x of x_count


economy = {}
for i in range(60):
    economy[i] = 0
economy[10] = 1000

people = {}
for i in range(1000):
    people[i] = 10


plt.bar(*zip(*economy.items()))
plt.show()


'''
def trading(i):
    trader0 = random.randint(0, individual_count-1)
    trader1 = random.randint(0, individual_count-1)

    # if 1, trader 1 wins $1 else trader 0
    coinflip = random.randint(0,1)


    plt.cla()
    count[1] += 10
    plt.bar(x, count)
    plt.xlabel("Money Dollars")
    plt.ylabel("Individuals")
    


def main() -> int: 

    fig = plt.figure(figsize = (10, 5))

    

    ani = FuncAnimation(plt.gcf(), trading, interval=1000)
    plt.show()
    

    return 0




if __name__ == '__main__':
    exit(main())

'''
