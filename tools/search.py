import os

f = open('search_list.txt').readlines()[900:1000]
for line in f:
    params = line.strip()
    command = 'sh scripts/slurm_train.sh ad_lidar {} 8 --cfg_file cfgs/kitti_models/pointpillar.yaml --max_ckpt_save_num 9' \
              ' --ckpt_save_interval 1 --extra_tag {}'.format(params, params)
    print(command)

    os.system(command)
