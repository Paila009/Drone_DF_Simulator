clc;
close all;
clear;
% Drone Position
drone = [100 50 30];

% Antennas

A = [0 0 5];
B = [-5 0 0];
C = [5 0 0];
D = [0 0 -5];

figure;

for r = 1:120

    clf

    hold on
    grid on
    axis equal

    % Drone
    scatter3(drone(1),drone(2),drone(3),300,'r','filled')

    % Antennas
    scatter3(A(1),A(2),A(3),150,'b','filled')
    scatter3(B(1),B(2),B(3),150,'b','filled')
    scatter3(C(1),C(2),C(3),150,'b','filled')
    scatter3(D(1),D(2),D(3),150,'b','filled')

    % Expanding RF Wave

    [x,y,z] = sphere(50);

    surf(...
        drone(1)+r*x,...
        drone(2)+r*y,...
        drone(3)+r*z,...
        'FaceAlpha',0.05,...
        'EdgeColor','g');

    text(drone(1),drone(2),drone(3),' DRONE')

    text(A(1),A(2),A(3),' ANT A')
    text(B(1),B(2),B(3),' ANT B')
    text(C(1),C(2),C(3),' ANT C')
    text(D(1),D(2),D(3),' ANT D')

    xlabel('X')
    ylabel('Y')
    zlabel('Z')

    title('RF Signal Propagation')

    axis([-50 150 -50 100 -50 100])

    view(3)

    drawnow

    pause(0.03)

end