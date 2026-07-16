function dir = directionEstimator(az)

az = mod(az,360);

if az >= 337.5 || az < 22.5
    dir = 'North';

elseif az < 67.5
    dir = 'North-East';

elseif az < 112.5
    dir = 'East';

elseif az < 157.5
    dir = 'South-East';

elseif az < 202.5
    dir = 'South';

elseif az < 247.5
    dir = 'South-West';

elseif az < 292.5
    dir = 'West';

else
    dir = 'North-West';

end

end