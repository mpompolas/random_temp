

choice = 'HASSAN'

LV1_ME     = load('C:/Users/McGill/Desktop/V1 scouts/scout_LV1_ME.mat');
RV1_ME     = load('C:/Users/McGill/Desktop/V1 scouts/scout_RV1_ME.mat');
LV1_HASSAN = load('C:/Users/McGill/Desktop/V1 scouts/scout_LV1_HASSAN.mat');
RV1_HASSAN = load('C:/Users/McGill/Desktop/V1 scouts/scout_RV1_HASSAN.mat');


% 
% a = zeros(20368,1);
% 
% for isource = 1:20368
%     
%     a(isource) = length(new_offset_from_threshold_unique{isource}(3,:));
% end

if strcmp(choice,'ME')
    indices = [LV1_ME.Scouts.Vertices RV1_ME.Scouts.Vertices];
    load('F:/Reverse Correlation/Me_high_resolution/iframes_crossing_NEGATIVE_3std_threshold.mat')
elseif strcmp(choice,'HASSAN')
    indices = [LV1_HASSAN.Scouts.Vertices RV1_HASSAN.Scouts.Vertices];
    load('F:/Reverse Correlation/Hassan_high_resolution/iframes_crossing_NEGATIVE_3std_threshold_revision_head_alignment.mat')
end
    
all_latencies = [];
for isource = indices
    disp(isource)
    all_latencies = [all_latencies new_offset_from_threshold_unique{isource}(3,:)];
end


save(['all_latencies_' choice '.mat'],'all_latencies')





%%

ME = load('all_latencies_ME.mat');
HASSAN = load('all_latencies_HASSAN.mat');

all_V1_latencies = [ME.all_latencies HASSAN.all_latencies];

figure;hist(all_V1_latencies*1000,100);
set(gca,'fontsize',20)
xlabel 'Latency (msec)'
title 'Histogram of V1 latencies of peak response'

