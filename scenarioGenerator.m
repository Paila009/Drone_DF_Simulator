function scenario = scenarioGenerator(params)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RF DF SIMULATOR
%
% SCENARIO GENERATOR
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Source Information

scenario.source = 'Drone';

scenario.signalType = 'CW';

scenario.modulation = 'OFDM';

%% RF Parameters

scenario.fc = params.fc;

scenario.bandwidth = params.bandwidth;

scenario.power = 1;

scenario.duration = 0.01;

scenario.SNR = params.SNR;

%% Direction Parameters

scenario.azimuth = params.trueAzimuth;

scenario.elevation = params.trueElevation;

%% Sampling

scenario.fs = params.fs;

scenario.snapshots = params.snapshots;

%% Display

disp(' ')
disp('SCENARIO CREATED')
disp(' ')

fprintf('Source       : %s\n',scenario.source);

fprintf('Modulation   : %s\n',scenario.modulation);

fprintf('Bandwidth    : %.2f MHz\n',scenario.bandwidth/1e6);

fprintf('SNR          : %.2f dB\n',scenario.SNR);

fprintf('Azimuth      : %.2f deg\n',scenario.azimuth);

fprintf('Elevation    : %.2f deg\n',scenario.elevation);

fprintf('\n');

end