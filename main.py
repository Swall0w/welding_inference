import imageio
import pandas as pd
from skimage import io

from welding.convert import convert_time_to_index, parse_time
from welding.replace import add_hour, iterative_hour_to_series


def main():
    videofile = 'data/output.mp4'
    txtfile = 'data/input.txt'

    dataframe = pd.read_csv(txtfile, delimiter='\t')
    vid = imageio.get_reader(videofile, 'ffmpeg')
    fps = vid.get_meta_data()['fps']

    time = dataframe['Weld Time'][1]
    print(time)
    a = parse_time(time)
    index = convert_time_to_index(a, fps)
    img = vid.get_data(index)
    print(img.shape)
    io.imshow(img)
    io.show()
    dataframe['Weld Time'] = dataframe['Weld Time'].apply(add_hour)
    dataframe['Weld Time'] = iterative_hour_to_series(dataframe['Weld Time'])
    print(dataframe['Weld Time'])


if __name__ == '__main__':
    main()
