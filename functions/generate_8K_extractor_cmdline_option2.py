import os
import sys

qp_dic = [22, 27, 32, 37, 42]
qp_name_dic = ["QP22", "QP27", "QP32", "QP37", "QP42"]
chunk_dic = ["0-31", "32-63", "64-95", "96-127", "128-159", "160-191", "192-223", "224-255", "256-287", "288-299"]
frameskip_dic = ["0", "32", "64", "96", "128", "160", "192", "224", "256", "288"]
frame_dic = ["32", "32", "32", "32", "32", "32", "32", "32", "32", "12"]
num_frame = 300
option = "option2"

bitstream_dir = "enc_chunk/{}/files_encoded/"
tile_dir = "enc_chunk/{}/extractor/option2/files_extracted/"
cfg_dir = "enc_chunk/{}/extractor/option2/config_files/"
log_dir = "enc_chunk/{}/extractor/option2/extractor_log/"

bitstream_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.265", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}.265",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.265"
]

tile_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}_tile{}.265", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}_tile{}.265",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}_tile{}.265"
]

log_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}_tile{}_extractor_log.txt", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}_tile{}_extractor_log.txt",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}_tile{}_extractor_log.txt"
]

# tile_dic structure:
# tile_dic[frame][tile_idx]

tile_dic = []

# chunk_tile_dic structure:
# chunk_tile_dic[chunk][tile_idx]

chunk_tile_dic = []

# Tilelist file example:
# Frame, number of tiles, tile indices
# 0, 6, 10, 11, 12, 15, 16, 17

def setTileList(tilelist_name):
	f = open(tilelist_name, 'r', encoding='utf-16')
	lines = f.readlines()
	f.close()

	# Skip first line
	for i in range(1, num_frame + 1):
		#print("i: " + str(i))
		#print(lines[i])
		data = lines[i].split()
		tile_dic.append([])

		for j in range(2, len(data)):
			tile_dic[i - 1].append(int(data[j]))

def setChunkTileList():
	for i in range(0, len(frameskip_dic)):
		startFrame = int(frameskip_dic[i])
		endFrame = startFrame + int(frame_dic[i])
		chunk_tile_dic.append([])

		for j in range(startFrame, endFrame):
			for k in range(0, len(tile_dic[j])):
				if tile_dic[j][k] not in chunk_tile_dic[i]:
					chunk_tile_dic[i].append(tile_dic[j][k])

		chunk_tile_dic[i] = sorted(chunk_tile_dic[i])


def extractor(cmd_name, tilelist_name):
	setTileList(tilelist_name)
	setChunkTileList()

	for c in range(0, len(chunk_dic)):
		chunk = chunk_dic[c]

		if not os.path.isdir("enc_chunk/" + chunk + "/extractor/" + option):
			os.mkdir("enc_chunk/" + chunk + "/extractor/" + option)
		if not os.path.isdir("enc_chunk/" + chunk + "/extractor/" + option + "/files_extracted/"):
			os.mkdir("enc_chunk/" + chunk + "/extractor/" + option + "/files_extracted/")
		if not os.path.isdir("enc_chunk/" + chunk + "/extractor/" + option + "/files_decoded/"):
			os.mkdir("enc_chunk/" + chunk + "/extractor/" + option + "/files_decoded/")
		if not os.path.isdir("enc_chunk/" + chunk + "/extractor/" + option + "/dec_log/"):
			os.mkdir("enc_chunk/" + chunk + "/extractor/" + option + "/dec_log/")
		if not os.path.isdir("enc_chunk/" + chunk + "/extractor/" + option + "/config_files/"):
			os.mkdir("enc_chunk/" + chunk + "/extractor/" + option + "/config_files/")
		if not os.path.isdir("enc_chunk/" + chunk + "/extractor/" + option + "/extractor_log"):
			os.mkdir("enc_chunk/" + chunk + "/extractor/" + option + "/extractor_log")

	cmd = open(cmd_name, 'w')
	
	for seq in range(0, len(bitstream_fmt_dic)):
		bitstream_fmt = bitstream_fmt_dic[seq]
		tile_fmt = tile_fmt_dic[seq]
		log_fmt = log_fmt_dic[seq]

		for c in range(0, len(chunk_dic)):
			chunk = chunk_dic[c]

			for q in range(0, len(qp_dic)):
				qp = str(qp_dic[q])
				qp_name = str(qp_name_dic[q])

				for tile in chunk_tile_dic[c]:	
					bitstream = bitstream_dir.format(chunk) + bitstream_fmt.format(qp, chunk)		
					tile_bitstream = tile_dir.format(chunk) + tile_fmt.format(qp, chunk, tile)	
					log = log_dir.format(chunk) + log_fmt.format(qp, chunk, tile)

					cmdline = "/data/vs/HEVC/HM-16.20/bin/TAppMCTSExtractorStatic"
					cmdline = cmdline + " -i " + bitstream
					cmdline = cmdline + " -b " + tile_bitstream
					cmdline = cmdline + " -d " + str(tile)
					cmdline = cmdline + " > " + log
					cmd.write(cmdline + "\n")
	
	cmd.close()


if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Usage : python generate_extractor_cmdline_AerialCity.py tilelist.txt run_command.sh")
        exit(0)
    else:
    	cmd_name = sys.argv[2]
    	tilelist_name = sys.argv[1]
    	extractor(cmd_name, tilelist_name)
    	print("Writing OK")

