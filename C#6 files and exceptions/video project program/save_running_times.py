def main():
    outfile = open('running_times.txt','w')
    vid_in_project = int(input('Enter number of videos in the project : '))
    for i in range(1,vid_in_project+1):
        vid_length= float(input('Video #' + str(i) + ': '))
        
        outfile.write(str(vid_length)+ '\n')
    outfile.close()
    print('Data has been written to running_times.txt.')
main()