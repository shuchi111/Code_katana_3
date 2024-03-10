def funcArrange(inputArr):
    evens = [x for x in inputArr if x % 2 == 0]
    odds = [x for x in inputArr if x % 2 != 0]
    return evens + odds

def main():
    inputArr = []
    inputArr_size = int(input())
    inputArr = list(map(int, input().split()))

    result = funcArrange(inputArr)
    print( " ".join(map(str, result)))

if __name__ == "__main__":
    main()
