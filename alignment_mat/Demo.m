close all; clc; clear;

addpath(genpath('./.'));
folder  = './.';                                                       % Put the image pairs in this folder
filepaths = dir(fullfile(folder, '*.png'));
 for i = 1:2:size(filepaths)
        I1  = im2double(imread(fullfile(folder,filepaths(i).name)));       % reference image
        I2  = im2double(imread(fullfile(folder,filepaths(i+1).name)));   % target image
 end
count = 0;
psnr_list = [];
temp_s = 2;
for s = 1.3:0.01:1.35     

       % s = 2.5;                                             % s = len1/len2, len1&lend2 are the focal length of captured image (len1>len2)
        r = 1 - 1/s;                                       % Scale
        I2_zoom = warpImg(I2,[-r,0,0,0]);
        psnr = psnrnumber(I1, I2_zoom);
        
        
       % fprintf('第%d次的裁切得到的psnr是%s\n', count, num2str(psnr));
        
        psnr_list = [psnr_list psnr];
        if length(psnr_list) >= 2
            if psnr_list(end) >= psnr_list(end-1)
                max_psnr = psnr_list(end);
                temp_s = s;
            end
        end
            
        %tau0 = zeros(6,1);
        %iter = 3;                                          % number of iterations

%        [I2_t,tau] = align_l(I2_zoom,I1,tau0,iter);
 %       [I2_t_l] = luminance_transfer(I1,I2_t);            % transfer luminance
  %      [I2_t_c] = color_transfer(I1,I2_t);                % transfer color

        % where you save the image
        
       imwrite(I1, ['./.', strcat(num2str(s),'_000086428(1)','.png')])            
       imwrite(I2_zoom, ['./.', strcat(num2str(s),'_000086428(2)','.png')])
       count = count + 0.1;
       
end