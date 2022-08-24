import os
import cv2
from skimage.metrics import peak_signal_noise_ratio as compare_psnr

ours_dir = '/home/wangyichen/fanbenchao/VideoDenoise/MAP_test/blind/Results/ours_blind_png'
MAP_dir = '/home/wangyichen/fanbenchao/VideoDenoise/MAP_test/blind/Results/denoising_45'
fastdvd_dir = '/home/wangyichen/compare_experiment/FastDVD_N/Results/blind_png'
gt_dir = '/data/vimeo'
out_dir = '/home/wangyichen/data/denoise/compare'
os.makedirs(out_dir, exist_ok=True)



noise_level_list = [[15, 0.30, 0.15], [20, 0.00, 0.30], [30, 0.20, 0.00]]
folder_list = ['00094', '00095', '00096']


for noise_level in noise_level_list:
    for folder in folder_list:
        ours_pic_dir = os.path.join(ours_dir, 'AWGN_%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder)
        MAP_pic_dir = os.path.join(MAP_dir, 'AWGN_%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder)
        fastdvd_pic_dir = os.path.join(fastdvd_dir, 'AWGN_%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder)
        gt_pic_dir = os.path.join(gt_dir, folder)

        ours_img_list = sorted(os.listdir(ours_pic_dir))
        MAP_img_list = sorted(os.listdir(MAP_pic_dir))
        fastdvd_img_list = sorted(os.listdir(fastdvd_pic_dir))
        gt_img_list = sorted(os.listdir(gt_pic_dir))

        print('fold %s is comparing' % folder)
        # 分别比较前三个文件夹里的图片与最后一个文件夹对应图片的psnr值

        for i in range(len(ours_img_list)):

            ours_img_path = os.path.join(ours_pic_dir, ours_img_list[i], 'im4.png')
            MAP_img_path = os.path.join(MAP_pic_dir, MAP_img_list[i], 'im4.png')
            fastdvd_img_path = os.path.join(fastdvd_pic_dir, fastdvd_img_list[i], 'im4.png')
            gt_img_path = os.path.join(gt_pic_dir, gt_img_list[i], 'im4.png')

            ours_img = cv2.imread(ours_img_path)
            MAP_img = cv2.imread(MAP_img_path)
            fastdvd_img = cv2.imread(fastdvd_img_path)
            gt_img = cv2.imread(gt_img_path)

            ours_psnr = compare_psnr(ours_img, gt_img)
            MAP_psnr = compare_psnr(MAP_img, gt_img)
            fastdvd_psnr = compare_psnr(fastdvd_img, gt_img)

            # 如果ours_psnr - MAP_psnr > 0.3且ours_psnr - fastdvd_psnr > 0.3，则将四张图片分别保存到out_dir下
            if ours_psnr - MAP_psnr > 0.3 and ours_psnr - fastdvd_psnr > 0.3 and ours_psnr - MAP_psnr < 5:
                print('ours_psnr:', ours_psnr)
                print('Map_psnr:', MAP_psnr)
                print('fastdvd_psnr:', fastdvd_psnr)
                cv2.imwrite(os.path.join(out_dir, 'AWGN%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder, 'folder%s_' % folder, ours_img_list[i] + '_ours.png'), ours_img)
                cv2.imwrite(os.path.join(out_dir, 'AWGN%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder, 'folder%s_' % folder, MAP_img_list[i] + '_MAP.png'), MAP_img)
                cv2.imwrite(os.path.join(out_dir, 'AWGN%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder, 'folder%s_' % folder, fastdvd_img_list[i] + '_fastdvd.png'), fastdvd_img)
                cv2.imwrite(os.path.join(out_dir, 'AWGN%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder, 'folder%s_' % folder, gt_img_list[i] + '_gt.png'), gt_img)
                file = open(os.path.join(out_dir, 'psnr.txt'), 'a+')
                file.write('folder %s_%dth pic: ours_psnr: %.4f (+%4f +%4f) MAP_psnr: %.4f fastdvd_psnr: %.4f \n' % (folder, i, ours_psnr, (ours_psnr - MAP_psnr), (ours_psnr - fastdvd_psnr), MAP_psnr, fastdvd_psnr))
                file.close()
                print('save %s successfully' % os.path.join(out_dir, 'AWGN%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder, 'folder%s_' % folder, ours_img_list[i] + '_ours.png'))
                print('save %s successfully' % os.path.join(out_dir, 'AWGN%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder, 'folder%s_' % folder, MAP_img_list[i] + '_MAP.png'))
                print('save %s successfully' % os.path.join(out_dir, 'AWGN%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder, 'folder%s_' % folder, fastdvd_img_list[i] + '_fastdvd.png'))
                print('save %s successfully' % os.path.join(out_dir, 'AWGN%d_SPIN%.2f_RVIN%.2f' % (noise_level[0], noise_level[1], noise_level[2]), folder, 'folder%s_' % folder, gt_img_list[i] + '_gt.png'))
        
            else:
                continue


