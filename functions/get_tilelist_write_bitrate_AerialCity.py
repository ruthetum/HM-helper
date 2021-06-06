# -*- coding: utf-8 -*-
import sys
import os

qp_dic = [22, 27, 32, 37]
qp_name_dic = ["QP22", "QP27", "QP32", "QP37"]

#chunk_dic = ["0-31", "32-63", "64-96"]
#view_dic = [0]
#pose_dic = ["Ap01", "Ap02", "Ap03"]
#chunk_size_dic = [32, 32, 33]
frame_number = 300
fps = 30

tile_bitstream_dir = "extractor/{}/files_extracted/"
tile_bitstream_fmt = "AerialCity_3840x1920_30fps_8bit_420_erp_{}_tile{}.265"
#tile_bitstream_fmt = "DrivingInCity_3840x1920_30fps_8bit_420_erp_{}_tile{}.265"
#"tile_bitstream_fmt = DrivingInCountry_3840x1920_30fps_8bit_420_erp_{}_tile{}.265"
bitstream_fmt = "AerialCity_3840x1920_30fps_8bit_420_erp_{}.265"

tile_dic = []

# Tilelist file example:
# Frame, number of tiles, tile indices
# 0, 6, 10, 11, 12, 15, 16, 17

def setTileList(tilelist_name):
    f = open(tilelist_name, 'r', encoding='utf-16')
    lines = f.readlines()
    f.close()

    data = lines[1].split()

    for i in range(2, len(data)):
        tile_dic.append(int(data[i]))

def tile_bitrate(tilesizelist_name, tilelist_name, bitrate_name):

    f = open(tilesizelist_name, 'r', encoding='utf-8')
    tilesizelist = f.readlines()
    f.close()

    setTileList(tilelist_name)

    bitrate_file = open(bitrate_name, 'w')

    for q in range(0, len(qp_dic)): 
        qp = str(qp_dic[q])
        qp_name = qp_name_dic[q]

        tile_bitstream_size = 0
        tile_bitstream_bitrate = 0
        tileData_found_flag = False

        bitstream = bitstream_fmt.format(qp)

        for tile in tile_dic:
            tile_bitstream = tile_bitstream_dir.format(qp_name) + tile_bitstream_fmt.format(qp, tile)

            for i in range(0, len(tilesizelist)):
                tileData = tilesizelist[i].split()
                tilename = tileData[-1]

                if tile_bitstream in tilename:
                    tile_bitstream_size += int(tileData[4])
                    tileData_found_flag = True
                    break

        if tileData_found_flag == True:
            tile_bitstream_bitrate = ((fps * (tile_bitstream_size / frame_number)) / 1000) * 8
            bitrate_file.write(bitstream + ", " + str(tile_bitstream_bitrate) + "\n")

    bitrate_file.close()

if __name__ == '__main__':
    if(len(sys.argv) != 4):
        print("Usage : python get_tilelist_write_bitrate_AerialCity.py tilesizelist_3x6_AerialCity.txt tilelist_3x6_AerialCity.txt tile_bitrate_3x6_AerialCity.csv ")
        print("This program gets tilelist, tile size list and writes bitrate.")
        exit(0)

    tilesizelist_name = sys.argv[1]
    tilelist_name = sys.argv[2]
    bitrate_name = sys.argv[3]

    tile_bitrate(tilesizelist_name, tilelist_name, bitrate_name)
    print("Writing OK")