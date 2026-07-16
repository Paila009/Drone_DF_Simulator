function wavefrontAnimation(array,az,el,params)

figure;

set(gcf,'Color',params.bgColor);

hold on;

grid on;

axis equal;

xlabel('X');

ylabel('Y');

zlabel('Z');

title('Incoming RF Plane Waves','Color','w');

set(gca,'Color',params.bgColor);

scatter3( ...
    array.positions(:,1), ...
    array.positions(:,2), ...
    array.positions(:,3), ...
    300, ...
    params.arrayColor, ...
    'filled');

for i=1:array.numElements

    text( ...
        array.positions(i,1), ...
        array.positions(i,2), ...
        array.positions(i,3)+0.01, ...
        array.labels{i}, ...
        'Color','w');

end

ux = cosd(el)*cosd(az);

uy = cosd(el)*sind(az);

uz = sind(el);

for k = 1:params.wavefronts

    p = 2 - k*0.15;

    x = p*ux;

    y = p*uy;

    z = p*uz;

    plot3( ...
        [x-0.25 x+0.25], ...
        [y-0.25 y+0.25], ...
        [z z], ...
        'Color',params.waveColor, ...
        'LineWidth',2);

    pause(params.animationSpeed);

    drawnow;

end

quiver3( ...
    0, ...
    0, ...
    0, ...
    ux, ...
    uy, ...
    uz, ...
    1.5, ...
    'Color',params.signalColor, ...
    'LineWidth',3);

scatter3(0,0,0,300,'w','filled');

view(45,25);

end