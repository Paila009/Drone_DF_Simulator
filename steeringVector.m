function a = steeringVector(array, az, el, params)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% STEERING VECTOR
%
% Calculates phase shifts across antenna array
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fc = params.fc;

c = params.c;

lambda = c / fc;

k = (2*pi) / lambda;

az = deg2rad(az);

el = deg2rad(el);

u = [

cos(el)*cos(az)

cos(el)*sin(az)

sin(el)

];

positions = array.positions;

N = size(positions,1);

a = zeros(N,1);

for n = 1:N

    phase = k * dot(positions(n,:),u);

    a(n) = exp(-1j*phase);

end

disp(' ')

disp('STEERING VECTOR GENERATED')

disp(' ')

disp(a)

end