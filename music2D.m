function [Pmusic,AZ,EL] = music2D(R,array,params)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% 2D MUSIC ALGORITHM
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp(' ')
disp('RUNNING MUSIC')
disp(' ')

azScan = params.azimuthScan;

elScan = params.elevationScan;

AZ = azScan;
EL = elScan;

numAz = length(AZ);

numEl = length(EL);

Pmusic = zeros(numEl,numAz);

%% Eigen Decomposition

[V,D] = eig(R);

eigenValues = diag(D);

[eigenValues,idx] = sort(eigenValues,'descend');

V = V(:,idx);

numSignals = params.numSignals;

En = V(:,numSignals+1:end);

%% MUSIC Spectrum

for i = 1:numAz

    az = AZ(i);

    for j = 1:numEl

        el = EL(j);

        a = steeringVector( ...
            array,...
            az,...
            el,...
            params);

        denom = a'*(En*En')*a;

        Pmusic(j,i) = 1/abs(denom);

    end

end

Pmusic = 10*log10(Pmusic);

disp('MUSIC COMPLETE')

fprintf('\n')

fprintf('Azimuth Points : %d\n',numAz);

fprintf('Elevation Points : %d\n',numEl);

fprintf('\n')

end