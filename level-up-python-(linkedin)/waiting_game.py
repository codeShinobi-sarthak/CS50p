import time
from random import randint

def waiting_game():
    random_time = randint(1, 9)
    print("you have to wait for", random_time, "seconds.")
    print("------- press enter to continue -------")
    input()
    while(True):
        start_time = time.perf_counter()
        input()
        end_time = time.perf_counter()
        print("Elapsed time :", end_time - start_time)
        if end_time - start_time == random_time:
            print("Well done!")
            break
        elif end_time - start_time > random_time:
            print("Too late! -> ", random_time - (end_time - start_time), "seconds.")
            break
        elif end_time - start_time < random_time:
            print("Too fast! -> ", random_time - (end_time - start_time), "seconds.")
            break

if __name__ == "__main__":
    waiting_game()