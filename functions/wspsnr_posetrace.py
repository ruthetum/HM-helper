# -*- coding: utf-8 -*-
import sys
import os

qp_dic = [22, 27, 32, 37, 42]
qp_name_dic = ["QP22", "QP27", "QP32", "QP37", "QP42"]
pose_dic = ["option1", "option2"]

org_yuv_dir = "/data/vs/VRTestSequence/JVET-E0024/"
cfg_dir = "wspsnr_cfg/"
log_dir = "wspsnr_log/"

org_yuv_fmt_dic = ["Gaslamp_2048x2048_30fps_300frames_8bits_420_erp_{}.yuv", 
"Harbor_2048x2048_30fps_8bit_420_erp_{}.yuv",
"Trolley_2048x2048_30fps_300frames_8bits_420_erp_{}.yuv"
]

rec_yuv_fmt_dic = ["Gaslamp_2048x2048_30fps_300frames_8bits_420_erp_{}_{}.yuv", 
"Harbor_2048x2048_30fps_8bit_420_erp_{}_{}.yuv",
"Trolley_2048x2048_30fps_300frames_8bits_420_erp_{}_{}.yuv"
]

cfg_fmt_dic = ["Gaslamp_2048x2048_30fps_300frames_8bits_420_erp_{}_{}_wspsnr_cfg.json", 
"Harbor_2048x2048_30fps_8bit_420_erp_{}_{}_wspsnr_cfg.json",
"Trolley_2048x2048_30fps_300frames_8bits_420_erp_{}_{}_wspsnr_cfg.json"
]

log_fmt_dic = ["Gaslamp_2048x2048_30fps_300frames_8bits_420_erp_{}_{}_wspsnr_log.txt", 
"Harbor_2048x2048_30fps_8bit_420_erp_{}_{}_wspsnr_log.txt",
"Trolley_2048x2048_30fps_300frames_8bits_420_erp_{}_{}_wspsnr_log.txt"
]

def wspsnr(cmd_name):

    width = "2048"
    height = "2048"
    start_frame = "0"
    number_of_frames = "300"
    
    cmd = open(cmd_name, 'w')
    log_filename = cmd_name.rstrip(".sh") + "_wspsnr_log_list.txt"
    log_file = open(log_filename, 'w')

    if not os.path.isdir(cfg_dir):
        os.mkdir(cfg_dir)
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)


    for seq in range(0, len(org_yuv_fmt_dic)):
        org_yuv_fmt = org_yuv_fmt_dic[seq]
        rec_yuv_fmt = rec_yuv_fmt_dic[seq]
        cfg_fmt = cfg_fmt_dic[seq]
        log_fmt = log_fmt_dic[seq]

        for q in range(0, len(qp_dic)):
            qp = str(qp_dic[q])
            qp_name = qp_name_dic[q]

            for p in range(0, len(pose_dic)):
                pose = pose_dic[p]

                org_yuv = org_yuv_dir + org_yuv_fmt.format(pose)
                rec_yuv = rec_yuv_fmt.format(qp, pose)
                cfg = cfg_dir + cfg_fmt.format(qp, pose)
                log = log_dir + log_fmt.format(qp, pose)

                log_file.write(log + '\n')
                f= open(cfg, 'w')
                f.write('{\n')
                f.write('\t"Version": "2.0.1",\n')
                f.write('\t"Projection": "Perspective",\n')
                f.write('\t"Original_file_path": "' + org_yuv + '",\n')
                f.write('\t"Reconstructed_file_path": "' + rec_yuv + '",\n')
                f.write('\t"ColorSpace": "YUV420",\n')
                f.write('\t"Video_width": ' + width + ',\n')
                f.write('\t"Video_height": ' + height + ',\n')
                f.write('\t"BitDepth": 8,\n')
                f.write('\t"StartFrame": ' + start_frame + ',\n')
                f.write('\t"NumberOfFrames": ' + number_of_frames + '\n')
                f.write('}\n')

                cmdline = "/data/vs/WSPSNR/wspsnr-v2.0.1/WSPSNR"
                cmdline = cmdline + " " + cfg
                cmdline = cmdline + " > " + log
                #print(cmdline)
                cmd.write(cmdline + '\n')

    cmd.close()
    log_file.close()


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage : python wspsnr_posetrace.py run_command.sh")
        exit(0)
    else:
        cmd_name = sys.argv[1]
        wspsnr(cmd_name)
        print("Writing OK")


    

