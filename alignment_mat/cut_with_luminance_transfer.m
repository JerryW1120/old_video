function [] = cut_with_the_luminance_transfer(genarate_path, waiting_to_be_cut_dir, reference_dir, save_dir)

addpath(genpath(genarate_path));
%addpath(genpath('E:\'));
folder_waiting_to_be_cut  = waiting_to_be_cut_dir;                                                        % Put the image pairs in this folder
filepaths_og = dir(fullfile(folder_waiting_to_be_cut, '*.png'));
folder_reference = reference_dir;
filepaths_fixed = dir(fullfile(folder_reference, '*.png'));


for i = 1:size(filepaths_og)
    I1  = im2double(imread(fullfile(folder_fixed,filepaths_reference(i).name)));       % reference image
    I2  = im2double(imread(fullfile(folder_og,filepaths_waiting_to_be_cut(i).name)));     % target image

    s = 1.886976;                                             % s = len1/len2, len1&lend2 are the focal length of captured image (len1>len2)
    r = 1 - 1/s;                                       % Scale
    I2_zoom = warpImg(I2,[-r,0,0,0]);
    
    tau0 = zeros(6,1);
    iter = 3;                                          % number of iterations

    %[I2_t,tau] = align_l(I2_zoom,I1,tau0,iter);
    %[I2_t_l] = luminance_transfer(I1,I2_zoom);            % transfer luminance
    [I2_t_c] = color_transfer(I1,I2_zoom);                % transfer color

    % where you save the image
    %imwrite(I1, ['./.', filepaths(i).name])            
    imwrite(I2_t_c, [save_dir, '\', filepaths_waiting_to_be_cut(i).name])
end

end