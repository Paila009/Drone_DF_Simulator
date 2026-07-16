function musicViewer(Pmusic,AZ,EL,azEst,elEst,params)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% MUSIC SPECTRUM VIEWER
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

figure;

set(gcf,'Color',params.bgColor);

imagesc(AZ,EL,Pmusic);

axis xy;

xlabel('Azimuth (deg)');
ylabel('Elevation (deg)');

title('2D MUSIC Spectrum');

colormap(jet);

colorbar;

hold on;

scatter(...
    azEst,...
    elEst,...
    200,...
    'w',...
    'filled');

text(...
    azEst+3,...
    elEst,...
    sprintf('(%.1f°, %.1f°)',...
    azEst,...
    elEst),...
    'Color','white',...
    'FontSize',12);

set(gca,...
    'Color',params.bgColor,...
    'XColor','white',...
    'YColor','white');

grid on;

end