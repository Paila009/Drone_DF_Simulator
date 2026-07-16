function R = covarianceMatrix(X)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% COVARIANCE MATRIX
%
% Computes spatial covariance matrix
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

L = size(X,2);

R = (X*X')/L;

disp(' ')
disp('COVARIANCE MATRIX COMPUTED')
disp(' ')

fprintf('Matrix Size : %d x %d\n',size(R,1),size(R,2));

fprintf('\n')

end