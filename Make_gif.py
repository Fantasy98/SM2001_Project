import imageio
def Draw_gif(T_start,T_end):
    with imageio.get_writer("Flow_{}_{}.gif".format(T_start,T_end),mode="I") as writer:
        for i in range(T_start,T_end):
            image = imageio.imread("/Users/wangyuning/Desktop/Data-driven Methods in Engineering Mechanics/SM2001_Project/Visualizing Data/Mid_Line_contour@t={}.png".format(i))
            writer.append_data(image) 