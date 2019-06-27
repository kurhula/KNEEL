import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_root', default='/media/lext/FAST/knee_landmarks/workdir/low_cost_data')
    parser.add_argument('--workdir', default='/media/lext/FAST/knee_landmarks/workdir')
    parser.add_argument('--metadata', default='bf_landmarks_1_0.3.csv')
    parser.add_argument('--annotations', type=str, choices=['hc', 'lc'], default='lc')
    parser.add_argument('--base_width', type=int, default=24)
    parser.add_argument('--n_folds', type=int, default=5)
    parser.add_argument('--n_epochs', type=int, default=100)
    parser.add_argument('--optimizer', choices=['sgd', 'adam'], default='adam')
    parser.add_argument('--swa_start', type=int, default=2)
    parser.add_argument('--swa_freq', type=int, default=2)
    parser.add_argument('--swa_lr', type=float, default=1e-3)
    parser.add_argument('--fold', type=int, default=-1)
    parser.add_argument('--loss_type', choices=['elastic', 'mse', 'wing', 'robust'], default='wing')
    parser.add_argument('--alpha_robust', type=float, default=1.)
    parser.add_argument('--c_robust', type=float, default=1e-2)
    parser.add_argument('--alpha_robust_min', type=float, default=0.)
    parser.add_argument('--alpha_robust_max', type=float, default=2.)
    parser.add_argument('--multiscale_hg', type=bool, default=False)
    parser.add_argument('--wing_w', type=float, default=15)
    parser.add_argument('--wing_c', type=float, default=3)
    parser.add_argument('--loss_weight', type=float, default=0.5)
    parser.add_argument('--start_val', type=int, default=-1)
    parser.add_argument('--lr_drop', nargs='+', default=[50, 80], type=int)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--img_pad', type=int, default=100)
    parser.add_argument('--wd', type=float, default=5e-5)
    parser.add_argument('--bs', type=int, default=32)
    parser.add_argument('--val_bs', type=int, default=16)
    parser.add_argument('--n_threads', type=int, default=8)
    parser.add_argument('--hc_spacing', type=float, default=0.3)
    parser.add_argument('--lc_spacing', type=int, default=1)
    parser.add_argument('--crop_y', type=int, default=430)
    parser.add_argument('--crop_x', type=int, default=180)
    parser.add_argument('--pad_x', type=int, default=200)
    parser.add_argument('--pad_y', type=int, default=500)
    parser.add_argument('--skip_train', type=int, default=1)
    parser.add_argument('--seed', type=int, default=42)
    return parser.parse_args()
