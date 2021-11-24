function [] = cut_the_picture(genarate_path, input_dir, save_dir)

close all; clc; clear;

addpath(genpath(genarate_path));
folder  = input_dir;                                                       % Put the image pairs in this folder
filepaths = dir(fullfile(folder, '*.png'));
for i = 1:size(filepaths)
        I1  = im2double(imread(fullfile(folder,filepaths(i).name)));
        I111=imcrop(I1,[514,116,1103,823]);
        imwrite(I111, [save_dir, '\', filepaths(i).name])
        % reference image
                % target image
end
        
%I11=imcrop(I2,[515,113,1105,825]);

%imshow(I2);

% figure

% imshow(I11);
        
%figure

% imshow(I111);

        
%black = zeros(1080,1920);
% black(150:250,150:250) = 1;
%figure
%imshow(black);
%imwrite(black, ['./.', ('black.png')])
end