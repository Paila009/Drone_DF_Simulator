function params = config()

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RF DF SIMULATOR CONFIGURATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Physical Constants

params.c = 3e8;

%% RF Parameters

params.fc = 2.4e9;

params.lambda = params.c / params.fc;

params.bandwidth = 20e6;

params.fs = 10e6;

params.SNR = 20;

params.snapshots = 2048;

%% Array Parameters

params.numElements = 4;

params.spacing = params.lambda/2;

params.geometry = 'Cross';

%% Ground Truth

params.trueAzimuth = 42;

params.trueElevation = 18;

%% Visualization

params.theme = 'dark';

params.wavefronts = 15;

params.animationSpeed = 0.02;

params.gridSize = 150;

%% Colors

params.bgColor = [0.05 0.05 0.08];

params.arrayColor = [0 0.7 1];

params.waveColor = [0 1 0.5];

params.signalColor = [1 0.4 0.1];

params.textColor = [1 1 1];

%% MUSIC Parameters

params.azimuthScan = 0:1:360;

params.elevationScan = 0:1:90;

params.numSignals = 1;

%% Display

fprintf('\n');

disp('CONFIGURATION LOADED')

fprintf('\n');

fprintf('Frequency       : %.2f GHz\n',params.fc/1e9);

fprintf('Wavelength      : %.4f m\n',params.lambda);

fprintf('Spacing         : %.4f m\n',params.spacing);

fprintf('Elements        : %d\n',params.numElements);

fprintf('Azimuth Truth   : %.2f deg\n',params.trueAzimuth);

fprintf('Elevation Truth : %.2f deg\n',params.trueElevation);

fprintf('\n');

end