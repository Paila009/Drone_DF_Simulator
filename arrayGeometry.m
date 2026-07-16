function array = arrayGeometry(params)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% ARRAY GEOMETRY
%
% 2 x 2 Uniform Rectangular Array
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

d = params.spacing;

array.positions = [

-d/2   d/2    0;

d/2   d/2    0;

-d/2  -d/2    0;

d/2  -d/2    0

];

array.labels = {

'A1'

'A2'

'A3'

'A4'

};

array.numElements = 4;

array.spacing = d;

array.type = 'URA';

disp(' ')

disp('ARRAY CREATED')

disp(' ')

fprintf('Array Type : %s\n',array.type);

fprintf('Elements   : %d\n',array.numElements);

fprintf('Spacing    : %.4f m\n',array.spacing);

fprintf('\n')

disp('Coordinates')

disp(array.positions)

fprintf('\n')

end