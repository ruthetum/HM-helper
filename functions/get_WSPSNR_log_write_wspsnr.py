# -*- coding: utf-8 -*-
import sys
import os

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Usage : python get_WSPSNR_log_write_wspsnr.py wspsnr_log_filelist.txt  wspsnr.csv")
        print("This program extracts WSPSNR(YUV) from WSPSNR log.")
        exit(0)

    f = open(sys.argv[1], 'r')
    files = f.readlines()
    f.close()

    csv = open(sys.argv[2], 'w')
    csv.write("Filename, WS-PSNR_Y, WS-PSNR_U, WS-PSNR_V\n")
    print("Filename\tWS-PSNR_Y\tWS-PSNR_U\tWS-PSNR_V")

    for i in range(0, len(files)):
        f = open(files[i].rstrip("\n"), 'r')
        lines = f.readlines()
        f.close()
        for j in range(0, len(lines)):
            if "Average" in lines[j]:
                data = lines[j + 2].split()
                filename = files[i].rstrip("\n")
                y_wspsnr = data[-3]
                u_wspsnr = data[-2]
                v_wspsnr = data[-1]
                csv.write(filename + "," + y_wspsnr + "," + u_wspsnr + "," + v_wspsnr + "\n")
                print(filename + "\t" + y_wspsnr + "\t" + u_wspsnr + "\t" + v_wspsnr)
    
    csv.close()