# python3

def parallel_processing(n, m, data):

    # n - thread count 
    # m - job count
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    output = []

    t_count = []
    t_count = [0 for i in range(n)]

    time_moment = 0

    while m > 0:
        for current in range(n):
            if t_count[current] == 0 and data:
                output.append((current, time_moment))
                t_count[current] = data[0]
                data.pop(0)
                m -= 1
            elif t_count[current] > 0:
                t_count[current] -= 1

        time_moment += 1

    return output

def main():
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    n = 0
    m = 0
    input1 = list(map(int, input().split()))
    n = input1[0]
    m = input1[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()