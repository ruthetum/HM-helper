# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    if(len(sys.argv) != 4):
        print("Usage : python split_cmdline.py command.sh 15 run_command.sh")
        exit(0)

    bat_name = sys.argv[1]
    num_cmd = int(sys.argv[2])

    bat_file = open(bat_name, 'r')
    lines = bat_file.readlines()
    bat_file.close()

    num_lines = len(lines)

    # Parallelly execution shell script name
    run_file = sys.argv[3]
    run = open(run_file, 'w')

    # 반복은 줄이 40줄이고 15가 입력되었으면 3번 해야함
    for i in range(0, int(round(num_lines / num_cmd))):
        new_bat_name = bat_name.rstrip(".sh") + "-" + str(i + 1) + ".sh"
        print(new_bat_name)
        new_bat_file = open(new_bat_name, 'w')
        start = i * num_cmd
        end = 0
        if num_lines > (i + 1) * num_cmd:
            end = (i + 1) * num_cmd
        else:
            end = num_lines
        for j in range(start, end):
            print(lines[j])
            new_bat_file.write(lines[j])
        new_bat_file.close()
        run.write("./" + new_bat_name + "&\n")
    run.close()
