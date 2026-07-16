function [azEst,elEst] = peakEstimator(Pmusic,AZ,EL)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% PEAK ESTIMATOR
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp(' ')
disp('ESTIMATING DOA')
disp(' ')

[maxValue,index] = max(Pmusic(:));

[row,col] = ind2sub(size(Pmusic),index);

azEst = AZ(col);

elEst = EL(row);

fprintf('Estimated Azimuth : %.2f deg\n',azEst);

fprintf('Estimated Elevation : %.2f deg\n',elEst);

fprintf('\n')

end