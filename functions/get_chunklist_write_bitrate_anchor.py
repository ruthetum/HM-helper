# -*- coding: utf-8 -*-
import sys
import os

qp_dic = [22, 27, 32, 37, 42]
qp_name_dic = ["QP22", "QP27", "QP32", "QP37", "QP42"]
chunk_dic = ["0-31", "32-63", "64-95", "96-127", "128-159", "160-191", "192-223", "224-255", "256-287", "288-299"]
frameskip_dic = ["0", "32", "64", "96", "128", "160", "192", "224", "256", "288"]
frame_dic = ["32", "32", "32", "32", "32", "32", "32", "32", "32", "12"]
pose_dic = ["option1", "option2"]
tilesize_dic = ["2x4", "3x6", "6x12"]
num_frame = 300

fps = 30

bitstream_dir = "enc_chunk/{}/files_encoded/"

bitstream_fmt_dir = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.265", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}.265", 
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.265"
]

output_bitstream_fmt_dir = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_0-299.265", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_0-299.265", 
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_0-299.265"
]

def filelist_write_bitrate(chunklist_filename, output_filename):

    output = open(output_filename, 'w')

    f = open(chunklist_filename, "rt", encoding="UTF8")
    chunksizelist = f.readlines()
    f.close()

    
    for seq in range(0, len(bitstream_fmt_dir)):
        bitstream_fmt = bitstream_fmt_dir[seq]
        output_bitstream_fmt = output_bitstream_fmt_dir[seq]
        
        for q in range(0, len(qp_dic)):
            qp = str(qp_dic[q])
            qp_name = str(qp_name_dic[q])
            output_bitstream = output_bitstream_fmt.format(qp)

            bitstreamsize = 0.0

            for c in range(0, len(chunk_dic)):
                chunk = chunk_dic[c]
                bitstream = bitstream_dir.format(chunk) + bitstream_fmt.format(qp, chunk)

                for i in range(0, len(chunksizelist)):

                    if bitstream in chunksizelist[i]:

                        data = chunksizelist[i].split()
                        chunksize = float(data[4])
                        bitstreamsize += chunksize

            bitrate = ((fps * (bitstreamsize / num_frame)) / 1000) * 8
            output.write(output_bitstream + "," + str(bitrate) + "\n")

    output.close()

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Usage : python get_chunklist_write_bitrate_anchor.py chunklist_anchor.txt chunklist_anchor.csv ")
        print("This program gets chunklist, and writes bitrate.")
        exit(0)

    chunklist_filename = sys.argv[1]
    output_filename = sys.argv[2]

    filelist_write_bitrate(chunklist_filename, output_filename)
    print("Writing OK")