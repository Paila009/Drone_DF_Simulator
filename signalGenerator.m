function X = signalGenerator(array,scenario,params)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% SIGNAL GENERATOR
%
% Simulated received RF signal
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

N = array.numElements;

L = params.snapshots;

SNR = params.SNR;

%% Steering Vector

a = steeringVector( ...
    array,...
    scenario.azimuth,...
    scenario.elevation,...
    params);

%% Source Signal

s = randn(1,L) + 1j*randn(1,L);

s = s ./ norm(s);

%% Array Reception

X = a * s;

%% Noise

noise = randn(N,L) + 1j*randn(N,L);

noise = noise ./ norm(noise,'fro');

noisePower = 10^(-SNR/20);

X = X + noisePower*noise;

disp(' ')

disp('SIGNAL GENERATED')

disp(' ')

fprintf('Channels : %d\n',N);

fprintf('Snapshots : %d\n',L);

fprintf('SNR : %.2f dB\n',SNR);

fprintf('\n')

end