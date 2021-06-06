# -*- coding: utf-8 -*-
import sys
import os

qp_dic = [22, 27, 32, 37]
qp_name_dic = ["QP22", "QP27", "QP32", "QP37"]
chunk_dic = ["0-31", "32-63", "64-95", "96-127", "128-159", "160-191", "192-223", "224-255", "256-287", "288-299"]
frameskip_dic = ["0", "32", "64", "96", "128", "160", "192", "224", "256", "288"]
frame_dic = ["32", "32", "32", "32", "32", "32", "32", "32", "32", "12"]
pose_dic = ["option1", "option2"]
num_frame = 300
fps = 30


bitstream_dir = "enc_chunk/{}/viewport_extractor/files_extracted/"

bitstream_fmt_dir = ["AerialCity_3840x1920_30fps_8bit_420_erp_{}_{}_{}.265", 
"DrivingInCity_3840x1920_30fps_8bit_420_erp_{}_{}_{}.265", 
"DrivingInCountry_3840x1920_30fps_8bit_420_erp_{}_{}_{}.265", 
"PoleVault_le_3840x1920_30fps_8bit_420_erp_{}_{}_{}.265"
]

output_bitstream_fmt_dir = ["AerialCity_3840x1920_30fps_8bit_420_erp_{}_{}_0-299_{}.265", 
"DrivingInCity_3840x1920_30fps_8bit_420_erp_{}_{}_0-299_{}.265", 
"DrivingInCountry_3840x1920_30fps_8bit_420_erp_{}_{}_0-299_{}.265", 
"PoleVault_le_3840x1920_30fps_8bit_420_erp_{}_{}_0-299_{}.265"
]

def viewport_tile_bitrate(tilelist_filename, tilesize, output_filename):

    output = open(output_filename, 'w')

    f = open(tilelist_filename, "rt", encoding="UTF8")
    chunksizelist = f.readlines()
    f.close()

    for seq in range(0, len(bitstream_fmt_dir)):
        bitstream_fmt = bitstream_fmt_dir[seq]
        output_bitstream_fmt = output_bitstream_fmt_dir[seq]

        for p in range(0, len(pose_dic)):
            pose = pose_dic[p]

            for q in range(0, len(qp_dic)):
                qp = str(qp_dic[q])
                qp_name = str(qp_name_dic[q])

                output_bitstream = output_bitstream_fmt.format(tilesize, qp, pose)
                bitstreamsize = 0.0

                for c in range(0, len(chunk_dic)):
                    chunk = chunk_dic[c]
                    bitstream = bitstream_dir.format(chunk) + bitstream_fmt.format(qp, chunk, pose)

                    for i in range(0, len(chunksizelist)):

                        if bitstream in chunksizelist[i]:

                            data = chunksizelist[i].split()
                            chunksize = float(data[4])
                            bitstreamsize += chunksize

                bitrate = ((fps * (bitstreamsize / num_frame)) / 1000) * 8
                output.write(output_bitstream + "," + str(bitrate) + "\n")

    output.close()

if __name__ == '__main__':
    if(len(sys.argv) != 4):
        print("Usage : python get_chunklist_write_bitrate_tile.py chunklist_2x4.txt 2x4 chunklist_2x4.csv")
        print("This program gets chunklist, and writes bitrate.")
        exit(0)

    tilelist_filename = sys.argv[1]
    tilesize = sys.argv[2]
    output_filename = sys.argv[3]

    viewport_tile_bitrate(tilelist_filename, tilesize, output_filename)
    print("Writing OK")