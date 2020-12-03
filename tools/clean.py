import os
import pickle

DIR_NAME = '/mnt/lustre/dingmingyu/Data_t1/OpenPCDet/output/kitti_models/pointpillar/'
file_list = open('/mnt/lustre/dingmingyu/Data_t1/OpenPCDet/tools/search_list.txt').readlines()
all_dirs = os.listdir(DIR_NAME)

models = []

f = open('train_list.txt', 'w')
for index, line in enumerate(file_list):
    line = line.strip().replace('3ddet', '3ddet')
    if line not in all_dirs:
        print('no such dirs', index, line)
        print(line, file=f)
        continue
    files = os.listdir(DIR_NAME + line + '/ckpt')
    if 'checkpoint_epoch_80.pth' not in files:
        print('!!!!!!!no final models', index, line)
        print(line, file=f)

        os.system('rm -rf %s' % (DIR_NAME + line))
        continue

    if os.path.exists(DIR_NAME + line + '/eval/eval_with_train/epoch_80/val/ap_dict.pkl'):
        print(index, line)
        os.system('rm -rf %s' % (DIR_NAME + line + '/tensorboard'))
        os.system('rm -rf %s' % (DIR_NAME + line + '/pointpillar.yaml'))
        os.system('rm -rf %s' % (DIR_NAME + line + '/eval/eval_with_train/eval_list_val.txt'))
        os.system('rm -rf %s' % (DIR_NAME + line + '/eval/eval_with_train/tensorboard_val'))
        os.system('rm -rf %s' % (DIR_NAME + line + '/eval/eval_with_train/*/val/result.pkl'))
        os.system('rm -rf %s' % (DIR_NAME + line + '/ckpt/*_optim.pth'))
    else:
        os.system('rm -rf %s' % (DIR_NAME + line))

#     if index > 10:
#         break

f.close()