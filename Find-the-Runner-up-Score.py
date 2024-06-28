if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = list(set(arr))
    result.sort()
    print(result[-2])
    
