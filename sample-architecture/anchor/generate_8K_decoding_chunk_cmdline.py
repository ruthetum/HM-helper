import os
import sys

qp_dic = [22, 27, 32, 37, 42]
qp_name_dic = ["QP22", "QP27", "QP32", "QP37", "QP42"]
chunk_dic = ["0-31", "32-63", "64-95", "96-127", "128-159", "160-191", "192-223", "224-255", "256-287", "288-299"]
frameskip_dic = ["0", "32", "64", "96", "128", "160", "192", "224", "256", "288"]
frame_dic = ["32", "32", "32", "32", "32", "32", "32", "32", "32", "12"]

bitstream_dir_fmt = "enc_chunk/{}/files_encoded/"
yuv_dir_fmt = "enc_chunk/{}/files_decoded/"
log_dir_fmt = "enc_chunk/{}/dec_log/"

bitstream_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.265", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}.265",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.265"
]

yuv_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.yuv", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}.yuv",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.yuv"
]

log_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}_dec_log.txt", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}_dec_log.txt",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}_dec_log.txt"
]

def decoding(cmd_name):

	cmd = open(cmd_name, 'w')

	for seq in range(0, len(bitstream_fmt_dic)):
		bitstream_fmt = bitstream_fmt_dic[seq]
		yuv_fmt = yuv_fmt_dic[seq]
		log_fmt = log_fmt_dic[seq]

		for c in range(0, len(chunk_dic)):
			chunk = chunk_dic[c]
			frameskip = frameskip_dic[c]
			frame = frame_dic[c]

			for q in range(0, len(qp_dic)):
				qp = str(qp_dic[q])
				qp_name = str(qp_name_dic[q])

				bitstream = bitstream_dir_fmt.format(chunk) + bitstream_fmt.format(qp, chunk)
				yuv = yuv_dir_fmt.format(chunk) + yuv_fmt.format(qp, chunk)
				log = log_dir_fmt.format(chunk) + log_fmt.format(qp, chunk)

				cmdline = "/data/vs/HM-16.20/HM-16.20/bin/TAppDecoderStatic"
				cmdline = cmdline + " -b " + bitstream
				cmdline = cmdline + " -o " + yuv
				cmdline = cmdline + " > " + log

				cmd.write(cmdline + "\n")
				
	cmd.close()


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage : python generate_8K_decoding_chunk_cmdline.py run_command.sh")
        exit(0)
    else:
    	cmd_name = sys.argv[1]
    	decoding(cmd_name)
    	print("Writing OK")

