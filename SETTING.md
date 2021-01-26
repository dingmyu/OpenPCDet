sh34

srun -p AD -n1 --gres=gpu:8 -c48 python -m pcdet.datasets.kitti.kitti_dataset create_kitti_infos tools/cfgs/dataset_configs/kitti_dataset.yaml

sh scripts/slurm_train.sh AD test 8 --cfg_file cfgs/kitti_models/pointpillar.yaml --max_ckpt_save_num 9 --ckpt_save_interval 1 --extra_tag seg-32_16-1_1_1_32-3_2_3_2_16_32-1_3_1_1_1_112_48_32-2_4_4_3_4_2_32_64_32_112-128

export PATH=/mnt/lustre/share/gcc/gcc-5.4/bin/:$PATH
export PATH=/mnt/lustre/share/cmake-3.11.0-Linux-x86_64/bin:$PATH

source /mnt/lustre/share/shishaoshuai/anaconda3/bin/activate base
export LD_LIBRARY_PATH=/mnt/lustre/share/shishaoshuai/anaconda3/lib/python3.7/site-packages/spconv/:$LD_LIBRARY_PATH
export NUMBAPRO_NVVM=/mnt/lustre/share/cuda-9.0/nvvm/lib64/libnvvm.so
export NUMBAPRO_LIBDEVICE=/mnt/lustre/share/cuda-9.0/nvvm/libdevice
export PYTHONPATH=./:$PYTHONPATH


sh36

export NUMBAPRO_NVVM=/mnt/lustre/share/cuda-9.0/nvvm/lib64/libnvvm.so
export NUMBAPRO_LIBDEVICE=/mnt/lustre/share/cuda-9.0/nvvm/libdevice
export PATH=/mnt/lustre/share/gcc/gcc-5.4/bin/:$PATH
export PATH=/mnt/lustre/share/cmake-3.11.0-Linux-x86_64/bin:$PATH
source /mnt/lustre/share/sunshuyang/anaconda3/bin/activate nus
export PYTHONPATH=/mnt/lustrenew/dingmingyu/data_t1/CVPR21/openpcdet:$PYTHONPATH
export LD_LIBRARY_PATH=/mnt/lustre/share/sunshuyang/spconv/:$LD_LIBRARY_PATH

srun -p ad_lidar -c48  python setup.py develop --user
ln -s /mnt/lustrenew/dingmingyu/data_t1/PCDet_poly/data/kitti kitti

sh scripts/slurm_train.sh ad_lidar supp1 4 --cfg_file cfgs/kitti_models/pointpillar.yaml --max_ckpt_save_num 9 --ckpt_save_interval 1 --extra_tag final-40_40-1_1_4_8-1_2_1_2_104_64-1_3_3_1_1_56_32_88-3_4_1_1_3_3_8_64_128_128-16


1984

export PATH=/mnt/lustre/dingmingyu/bin:$PATH
export PATH=/mnt/lustre/share/gcc/gcc-5.4/bin/:$PATH
export PATH=/mnt/lustre/share/cmake-3.11.0-Linux-x86_64/bin:$PATH
source /mnt/lustre/share_data/LOD/shishaoshuai/anaconda3/bin/activate base
export PYTHONPATH=/mnt/lustre/dingmingyu/2020/OpenPCDet:$PYTHONPATH
export LD_LIBRARY_PATH=/mnt/lustre/share_data/LOD/shishaoshuai/anaconda3/lib/python3.7/site-packages/spconv/:$LD_LIBRARY_PATH
export NUMBAPRO_NVVM=/mnt/lustre/share/cuda-9.0/nvvm/lib64/libnvvm.so
export NUMBAPRO_LIBDEVICE=/mnt/lustre/share/cuda-9.0/nvvm/libdevice
export PATH=/mnt/lustre/share/cuda-9.0/bin:$PATH
export LD_LIBRARY_PATH=/mnt/lustre/share/cuda-9.0/lib64/:$LD_LIBRARY_PATH


srun -p pat_moon -c24  python setup.py develop --user

srun -p pat_moon -n1 --gres=gpu:8 -c24 python -m pcdet.datasets.kitti.kitti_dataset create_kitti_infos tools/cfgs/dataset_configs/kitti_dataset.yaml


40

ln -s /mnt/lustre/share/shishaoshuai/anaconda3/bin/ld_temp ld

conda deactivate

export PATH=/mnt/lustre/dingmingyu/bin:$PATH
export PATH=/mnt/lustre/share/gcc/gcc-5.4/bin/:$PATH
export PATH=/mnt/lustre/share/cmake-3.11.0-Linux-x86_64/bin:$PATH
source /mnt/lustre/share/shishaoshuai/anaconda3/bin/activate base
export LD_LIBRARY_PATH=/mnt/lustre/share/shishaoshuai/anaconda3/lib/python3.7/site-packages/spconv/:$LD_LIBRARY_PATH
export NUMBAPRO_NVVM=/mnt/lustre/share/cuda-9.0/nvvm/lib64/libnvvm.so
export NUMBAPRO_LIBDEVICE=/mnt/lustre/share/cuda-9.0/nvvm/libdevice
export PYTHONPATH=./:$PYTHONPATH

srun -p AD -c24  python setup.py develop --user

ln -s /mnt/lustre/share/songxiao/3ddet/kitti/training training
ln -s /mnt/lustre/share/songxiao/3ddet/kitti/testing testing

srun -p AD -n1 --gres=gpu:8 -c24 python -m pcdet.datasets.kitti.kitti_dataset create_kitti_infos tools/cfgs/dataset_configs/kitti_dataset.yaml
