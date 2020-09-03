srun -p AD -n1 --gres=gpu:8 -c48 python -m pcdet.datasets.kitti.kitti_dataset create_kitti_infos tools/cfgs/dataset_configs/kitti_dataset.yaml

sh scripts/slurm_train.sh AD test 8 --cfg_file cfgs/kitti_models/pointpillar.yaml --max_ckpt_save_num 10 --ckpt_save_interval 1 --extra_tag mymodel

export PATH=/mnt/lustre/share/gcc/gcc-5.4/bin/:$PATH
export PATH=/mnt/lustre/share/cmake-3.11.0-Linux-x86_64/bin:$PATH

source /mnt/lustre/share/shishaoshuai/anaconda3/bin/activate base
export LD_LIBRARY_PATH=/mnt/lustre/share/shishaoshuai/anaconda3/lib/python3.7/site-packages/spconv/:$LD_LIBRARY_PATH
export NUMBAPRO_NVVM=/mnt/lustre/share/cuda-9.0/nvvm/lib64/libnvvm.so
export NUMBAPRO_LIBDEVICE=/mnt/lustre/share/cuda-9.0/nvvm/libdevice
export PYTHONPATH=./:$PYTHONPATH
