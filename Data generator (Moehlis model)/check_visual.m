load moehlis_data_1000.mat

for i = 1:10
    fig = figure(i);
    visualize_fields(reshape(data(i,:,:),4000,9));
    name = sprintf("%i",i);
    savefig(name)
    
end