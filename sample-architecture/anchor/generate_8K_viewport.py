import os
import sys

qp_dic = [22, 27, 32, 37, 42]
qp_name_dic = ["QP22", "QP27", "QP32", "QP37", "QP42"]
pose_dic = ["option1", "option2"]

concat_yuv_dir = "enc_chunk/concat/0-299/"
#concat_yuv_dir = "enc_chunk/0-29/files_decoded/"
viewport_dir = "enc_chunk/viewport/"
log_dir = "enc_chunk/viewport/viewport_log/"

width = 8192
height = 4096
CodingFaceWidth = 2048
CodingFaceHeight = 2048
framerate = 30
num_frame = 300

concat_yuv_fmt_dic = ["Gaslamp_8192x4096_30fps_300frames_8bits_420_erp_{}_0-299.yuv", 
"Harbor_8192x4096_30fps_8bit_420_erp_{}_0-299.yuv",
"Trolley_8192x4096_30fps_300frames_8bits_420_erp_{}_0-299.yuv"
]

cfg_fmt = "config_files/viewport_{}.txt"

viewport_fmt_dic = ["Gaslamp_2048x2048_30fps_300frames_8bits_420_erp_{}_{}.yuv", 
"Harbor_2048x2048_30fps_8bit_420_erp_{}_{}.yuv",
"Trolley_2048x2048_30fps_300frames_8bits_420_erp_{}_{}.yuv"
]

log_fmt_dic = ["Gaslamp_2048x2048_30fps_300frames_8bits_420_erp_{}_{}_viewport_log.txt", 
"Harbor_2048x2048_30fps_8bit_420_erp_{}_{}_viewport_log.txt",
"Trolley_2048x2048_30fps_300frames_8bits_420_erp_{}_{}_viewport_log.txt"
]

def viewport(cmd_name):

	if not os.path.isdir("enc_chunk/"):
		os.mkdir("enc_chunk/")
	if not os.path.isdir("enc_chunk/viewport/"):
		os.mkdir("enc_chunk/viewport/")
	if not os.path.isdir("enc_chunk/viewport/viewport_log/"):
		os.mkdir("enc_chunk/viewport/viewport_log/")
	
	cmd = open(cmd_name, 'w')
	log_filename = cmd_name.rstrip(".sh") + "_log_list.txt"
	log_file = open(log_filename, 'w')

	for seq in range(0, len(concat_yuv_fmt_dic)):
		concat_yuv_fmt = concat_yuv_fmt_dic[seq]
		viewport_fmt = viewport_fmt_dic[seq]
		log_fmt = log_fmt_dic[seq]

		for q in range(0, len(qp_dic)):
			qp = str(qp_dic[q])
			qp_name = str(qp_name_dic[q])

			for p in range(0, len(pose_dic)):
				pose = pose_dic[p]

				concat_yuv = concat_yuv_dir + concat_yuv_fmt.format(qp, pose)
				cfg = cfg_fmt.format(pose)
				viewport = viewport_dir + viewport_fmt.format(qp, pose)
				log = log_dir + log_fmt.format(qp, pose)
				cmdline = "/data/vs/360lib/360lib-5.1/HM-16.16/bin/TApp360ConvertStatic"
				cmdline = cmdline + " -i " + concat_yuv + " -c config_files/360test_DynamicViewports.cfg"
				cmdline = cmdline + " -v " + cfg + " -wdt " + str(width) + " -hgt " + str(height)
				cmdline = cmdline + " --CodingFaceWidth=" + str(CodingFaceWidth) + " --CodingFaceHeight=" + str(CodingFaceHeight)
				cmdline = cmdline + " -fr " + str(framerate) + " -f " + str(num_frame) + " -o " + viewport
				cmdline = cmdline + " > " + log
				cmd.write(cmdline + "\n")
				log_file.write(log + "\n")
				
	cmd.close()
	log_file.close()


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage : python generate_viewport.py run_command.sh")
        exit(0)
    else:
    	cmd_name = sys.argv[1]
    	viewport(cmd_name)
    	print("Writing OK")

