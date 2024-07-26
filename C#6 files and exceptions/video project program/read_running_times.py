def main():
    infile = open('running_times.txt','r')
    count = 0
    totalTime = 0
    for line in infile:
        time = float(line)
        count +=1
        totalTime += time
        print(f'Video # {count} : {time} seconds')
        
    infile.close()
    print(f'Total running time for {count} videos is {totalTime} seconds ')
main()
