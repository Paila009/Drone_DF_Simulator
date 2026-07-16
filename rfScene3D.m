function rfScene3D(array,azEst,elEst,params)

figure;

set(gcf,'Color',params.bgColor);

hold on;

grid on;

axis equal;

xlabel('X (m)');
ylabel('Y (m)');
zlabel('Z (m)');

title('RF Direction Finding Scene');

set(gca,'Color',params.bgColor);

scatter3( ...
    array.positions(:,1), ...
    array.positions(:,2), ...
    array.positions(:,3), ...
    250, ...
    params.arrayColor, ...
    'filled');

for i=1:array.numElements

    text( ...
        array.positions(i,1), ...
        array.positions(i,2), ...
        array.positions(i,3)+0.01, ...
        array.labels{i}, ...
        'Color','white');

end

x = cosd(elEst)*cosd(azEst);

y = cosd(elEst)*sind(azEst);

z = sind(elEst);

quiver3(0,0,0,x,y,z,1.5,...
    'Color',params.signalColor,...
    'LineWidth',3);

scatter3(0,0,0,250,'white','filled');

text(0,0,0.02,'CENTER','Color','white');

view(40,30);

end