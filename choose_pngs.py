import os
import cv2
from skimage.metrics import peak_signal_noise_ratio as compare_psnr

ours_dir = '/home/wangyichen/compare_experiment/remove_captions/Results/denoising_90'
BVD_dir = '/home/wangyichen/data/video_decaption/validation_png_used_for_test/output'
DVD_dir = '/home/wangyichen/data/video_decaption/validation_png_used_for_test/2021VD_test'
gt_dir = '/home/wangyichen/data/video_decaption/validation_png_used_for_test/Y'
out_dir = '/home/wangyichen/data/video_decaption/compare'
os.makedirs(out_dir, exist_ok=True)

ours_folder = sorted(os.listdir(ours_dir))
BVD_folder = sorted(os.listdir(BVD_dir))
DVD_folder = sorted(os.listdir(DVD_dir))
gt_folder = sorted(os.listdir(gt_dir))


for i in range(len(ours_folder)):
    # 取出四个文件夹里对应的图片
    ours_img_list = sorted(os.listdir(os.path.join(ours_dir, ours_folder[i])))
    BVD_img_list = sorted(os.listdir(os.path.join(BVD_dir, BVD_folder[i])))
    DVD_img_list = sorted(os.listdir(os.path.join(DVD_dir, DVD_folder[i])))
    gt_img_list = sorted(os.listdir(os.path.join(gt_dir, gt_folder[i])))
    print('fold %s is comparing' % ours_folder[i])
    # 分别比较前三个文件夹里的图片与最后一个文件夹对应图片的psnr值
    for j in range(len(ours_img_list)):
        ours_img_path = os.path.join(ours_dir, ours_folder[i], ours_img_list[j])
        BVD_img_path = os.path.join(BVD_dir, BVD_folder[i], BVD_img_list[j])
        DVD_img_path = os.path.join(DVD_dir, DVD_folder[i], DVD_img_list[j])
        gt_img_path = os.path.join(gt_dir, gt_folder[i], gt_img_list[j])
        ours_img = cv2.imread(ours_img_path)
        BVD_img = cv2.imread(BVD_img_path)
        DVD_img = cv2.imread(DVD_img_path)
        gt_img = cv2.imread(gt_img_path)
        ours_psnr = compare_psnr(ours_img, gt_img)
        BVD_psnr = compare_psnr(BVD_img, gt_img)
        DVD_psnr = compare_psnr(DVD_img, gt_img)
        
        # 如果ours_psnr - BVD_psnr > 0.3且ours_psnr - DVD_psnr > 0.3，则将四张图片分别保存到out_dir下
        if ours_psnr - BVD_psnr > 0.3 and ours_psnr - DVD_psnr > 0.3 and ours_psnr - BVD_psnr < 5 and BVD_psnr < DVD_psnr:
            print('ours_psnr:', ours_psnr)
            print('BVD_psnr:', BVD_psnr)
            print('DVD_psnr:', DVD_psnr, '\n')
            cv2.imwrite(os.path.join(out_dir, 'folder' + ours_folder[i][1:] + '_' + '%d_ours' % j + '.png'), ours_img)
            cv2.imwrite(os.path.join(out_dir, 'folder' + BVD_folder[i][1:] + '_' + '%d_BVD' % j + '.png'), BVD_img)
            cv2.imwrite(os.path.join(out_dir, 'folder' + DVD_folder[i][1:] + '_' + '%d_DVD' % j + '.png'), DVD_img)
            cv2.imwrite(os.path.join(out_dir, 'folder' + gt_folder[i][1:] + '_' + '%d_gt' % j + '.png'), gt_img)
            file = open(os.path.join(out_dir, 'psnr_v2.txt'), 'a+')
            file.write('folder %s_%dth pic: ours_psnr: %.4f (+%4f +%4f) BVD_psnr: %.4f DVD_psnr: %.4f \n' % (ours_folder[i][1:], j, ours_psnr, (ours_psnr - BVD_psnr), (ours_psnr - DVD_psnr), BVD_psnr, DVD_psnr))
            file.close()

            print('save %s successfully' % os.path.join(out_dir, 'ours_' + ours_folder[i] + '_' + 'ours_%d' % j + '.png'))
            print('save %s successfully' % os.path.join(out_dir, 'BVD_' + BVD_folder[i] + '_' + 'BVD_%d' % j + '.png'))
            print('save %s successfully' % os.path.join(out_dir, 'DVD_' + DVD_folder[i] + '_' + 'DVD_%d' % j + '.png'))
            print('save %s successfully' % os.path.join(out_dir, 'gt_' + gt_folder[i] + '_' + 'gt_%d' % j + '.png'))
        else:
            continue


