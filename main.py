import imageio
import pandas as pd
from skimage import io

from welding.convert import convert_time_to_index, parse_time
from welding.replace import add_hour, iterative_hour_to_series
import matplotlib.pyplot as plt
import numpy as np


def main():
    videofile = 'data/output.mp4'
    txtfile = 'data/input.txt'

    dataframe = pd.read_csv(txtfile, delimiter='\t')
    vid = imageio.get_reader(videofile, 'ffmpeg')
    fps = vid.get_meta_data()['fps']

    dataframe['Weld Time'] = dataframe['Weld Time'].apply(add_hour)
    dataframe['Weld Time'] = iterative_hour_to_series(dataframe['Weld Time'])
    max_index = 4138
    max_frame = 28

    image_list = []
    label_list = []

    for index, item in dataframe['Weld Time'].iteritems():
        current_video_index = convert_time_to_index(
            parse_time(item), fps)
        
        if index == max_index:
            next_video_index = current_video_index + max_frame
            break
        else:
            next_video_index = convert_time_to_index(
                parse_time(dataframe['Weld Time'][index+1]), fps)

#        img = vid.get_data(index).transpose(-1, 2, 0, 1).astype(np.float32) / 255.
        nums = [x for x in range(current_video_index, next_video_index)]
        for num in nums:
            #img = vid.get_data(num)
            img = vid.get_data(num).transpose(2, 0, 1).astype(np.float32) / 255.
            image_list.append(img)
            label_list.append(dataframe['w1_dy[mm]'][index])
    print(len(image_list), len(label_list))
#        print(index, video_index, dataframe['w1_dy[mm]'][index])
#        print(next_video_index - current_video_index)
#        print(index, max_index)


#    print(time)
#    img = vid.get_data(index)
#    print(img.shape)
#    io.imshow(img)
#    io.show()
#    dataframe['w1_dy[mm]'].plot()
#    print(dataframe['w1_dy[mm]'].as_matrix())
#    print(dataframe['Weld Time'].as_matrix())


if __name__ == '__main__':
    main()
