close all; clc; clear;

addpath(genpath('D:'));
all_folders_og = 'D:\og1';
all_folders_fixed = 'D:\fixed1';

all_files_og = genpath('D:\og1');
folders = strsplit(all_files_og, ';');

for folder = 2:214
    %裁切黑边
    folder_index = strsplit(string(folders(folder)), '\');
    folder_index = folder_index(3);
    save_dir_og = ['G:\og1\', folder_index];
    cut_the_picture(all_folders_og, string(folders(folder)), save_dir_og);

    %填充黑边使中心对齐
    py.put_the_pic_in_black.main_fuc(save_dir_og, save_dir_og);

    %带亮度的裁切，1.886976以修复画面为基准，裁填充后的原始画面得到og’
    reference_dir = [all_folders_fixed, '\', folder_index];
    cut_with_the_luminance_transfer(all_folders_og, save_dir_og, reference_dir, save_dir_og);


    %交替裁切，不调亮度,上一次的基准，这次是要被裁的，1.3以og’为基准，裁修复画面，得到fixed’
    save_fixed = ['G:\fixed1\', folder_index];
    Demo_og(all_folders_og, reference_dir, save_dir_og, save_fixed, rate)

end