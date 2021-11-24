import matlab
import matlab.engine

import put_the_pic_in_black as padding
import os

eng = matlab.engine.start_matlab()

eng.cd('F:\\Alignment', nargout = 0)

genarate_path = ('')

input_dir = 'H:\\000086400 - 000086879'
cut_dir = 'H:\\demo'


#裁切黑边
eng.cut_the_picture('H:\\', input_dir, cut_dir, nargout = 0)


#cut_files= os.listdir(cut_dir)
#cut_files.sort()

#填充黑边使中心对齐
padding_dir = 'H:\\demo_padding'
padding.main_fuc(cut_dir, padding_dir)

#带亮度的裁切
reference_dir = 'E:\000086400 - 000086879'
luminance_dir = 'H:\demo_luminance'
# cut_with_the_luminance_transfer(genarate_path, waiting_to_be_cut_dir, reference_dir, save_dir)
eng.cut_with_luminance_transfer('H:\\', padding_dir, reference_dir, luminance_dir, nargout = 0)



#交替裁切，不调亮度,上一次的基准，这次是要被裁的

second_cut_save_dir = 'H:\demo_1.3'
# Demo_og(genarate_path, waiting_to_be_cut_dir, reference_dir, save_dir, rate)
eng.Demo_og(genarate_path, reference_dir, luminance_dir, second_cut_save_dir, 1.3, nargout = 0)

eng.exit()









