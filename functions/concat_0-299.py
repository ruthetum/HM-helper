import os
import sys

qp_dic = [22, 27, 32, 37, 42]
chunk_dic = ["0-31", "32-63", "64-95", "96-127", "128-159", "160-191", "192-223", "224-255", "256-287", "288-299"]

decoded_yuv_dir_fmt = "enc_chunk/{}/files_decoded/"
concat_yuv_dir_fmt = "enc_chunk/concat/0-299/"

decoded_yuv_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.yuv", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_{}.yuv",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_{}.yuv"
]

concat_yuv_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_0-299.yuv", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_0-299.yuv",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_0-299.yuv"
]

def concat(cmd_name):
	cmd = open(cmd_name, 'w')
	
	for seq in range(0, len(decoded_yuv_fmt_dic)):
		decoded_yuv_fmt = decoded_yuv_fmt_dic[seq]
		concat_yuv_fmt = concat_yuv_fmt_dic[seq]
		
		for q in range(0, len(qp_dic)):
			qp = str(qp_dic[q])

			cmdline = "cat"
			
			for c in range(0, len(chunk_dic)):
				chunk = chunk_dic[c]
				decoded_yuv = decoded_yuv_dir_fmt.format(chunk) + decoded_yuv_fmt.format(qp, chunk)
				cmdline = cmdline + " " + decoded_yuv

			concat_yuv = concat_yuv_dir_fmt.format(chunk) + concat_yuv_fmt.format(qp)
			cmdline = cmdline + " > " + concat_yuv
			cmd.write(cmdline + "\n")
			
	cmd.close()
	
if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage : python concat_0-299_A.py run_command.sh")
        exit(0)
    else:
    	cmd_name = sys.argv[1]
    	concat(cmd_name)
    	print("Writing OK")
