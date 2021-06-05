import os
import sys

qp_dic = [22, 27, 32, 37, 42]
qp_name_dic = ["QP22", "QP27", "QP32", "QP37", "QP42"]
chunk_dic = ["0-31", "32-63", "64-95", "96-127", "128-159", "160-191", "192-223", "224-255", "256-287", "288-299"]
frameskip_dic = ["0", "32", "64", "96", "128", "160", "192", "224", "256", "288"]
frame_dic = ["32", "32", "32", "32", "32", "32", "32", "32", "32", "12"]

yuv_dic = ["/data/vs/VRTestSequence/Gaslamp_8192x4096_30fps_300frames_8bits_420_erp/Gaslamp_8192x4096_30fps_300frames_8bits_420_erp.yuv", 
"/data/vs/VRTestSequence/Harbor_8192x4096_30fps_8bit_420_erp/Harbor_8192x4096_30fps_8bit_420_erp.yuv",
"/data/vs/VRTestSequence/Trolley_8192x4096_30fps_300frames_8bits_420_erp/Trolley_8192x4096_30fps_300frames_8bits_420_erp.yuv"]
bitstream_dir_fmt = "enc_chunk/{}/files_encoded/"
log_dir_fmt = "enc_chunk/{}/enc_log/"

bitstream_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.265", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}.265",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.265"
]

log_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}_enc_log.txt", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}_enc_log.txt",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}_enc_log.txt",
]

seq_cfg = "config_files/8192x4096_32frames_cfg.cfg"
enc_cfg = "config_files/encoder_randomaccess_main.cfg"
width = "8192"
height = "4096"

def encoding(cmd_name):

	for c in range(0, len(chunk_dic)):
		chunk = chunk_dic[c]

		if not os.path.isdir("enc_chunk/"):
			os.mkdir("enc_chunk/")
		if not os.path.isdir("enc_chunk/" + chunk):
			os.mkdir("enc_chunk/" + chunk)
		if not os.path.isdir("enc_chunk/" + chunk + "/enc_log/"):
			os.mkdir("enc_chunk/" + chunk + "/enc_log/")
		if not os.path.isdir("enc_chunk/" + chunk + "/dec_log/"):
			os.mkdir("enc_chunk/" + chunk + "/dec_log/")
		if not os.path.isdir("enc_chunk/" + chunk + "/files_encoded/"):
			os.mkdir("enc_chunk/" + chunk + "/files_encoded/")
		if not os.path.isdir("enc_chunk/" + chunk + "/files_decoded/"):
			os.mkdir("enc_chunk/" + chunk + "/files_decoded/")
	
	cmd = open(cmd_name, 'w')
	log_filename = cmd_name.rstrip(".sh") + "_log_list.txt"
	log_file = open(log_filename, 'w')

	for seq in range(0, len(yuv_dic)):
		yuv = yuv_dic[seq]
		bitstream_fmt = bitstream_fmt_dic[seq]
		log_fmt = log_fmt_dic[seq]

		for c in range(0, len(chunk_dic)):
			chunk = chunk_dic[c]
			frameskip = frameskip_dic[c]
			frame = frame_dic[c]

			for q in range(0, len(qp_dic)):
				qp = str(qp_dic[q])
				qp_name = str(qp_name_dic[q])

				bitstream = bitstream_dir_fmt.format(chunk) + bitstream_fmt.format(qp, chunk)
				log = log_dir_fmt.format(chunk) + log_fmt.format(qp, chunk)

				cmdline = "/data/vs/HM-16.20/HM-16.20/bin/TAppEncoderStatic" + " -c " + seq_cfg + " -c " + enc_cfg
				cmdline = cmdline + " -i " + yuv
				cmdline = cmdline + " -b " + bitstream + " --SEIDecodedPictureHash=1"
				cmdline = cmdline + " -wdt " + width + " -hgt " + height
				cmdline = cmdline + " -fs " + frameskip + " -f " + frame + " -q " + qp
				cmdline = cmdline + " > " + log
				cmd.write(cmdline + "\n")
				log_file.write(log + "\n")
				
	cmd.close()
	log_file.close()


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage : python generate_8K_encoding_chunk_cmdline.py run_command.sh")
        exit(0)
    else:
    	cmd_name = sys.argv[1]
    	encoding(cmd_name)
    	print("Writing OK")

