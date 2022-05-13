if __name__ == "__main__":

    for i in range(1, 6):
        accept = [4 + 2 * num for num in range(1, i + 1)]
        print(accept)
        for j in range(i, i + 10):
            if j in accept:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(end="\n")
