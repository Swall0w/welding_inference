import imageio
import pandas as pd
from welding.convert import parse_time, convert_time_to_index


def main():
    videofile = 'data/output.mp4'
    txtfile = 'data/input.txt'

    dataframe = pd.read_csv(txtfile, delimiter='\t')
    vid = imageio.get_reader(videofile, 'ffmpeg')
    fps = vid.get_meta_data()['fps']
    print(fps)


    time = dataframe['Weld Time'][1]
    print(time)
    a = parse_time(time)
#    print(a.minute)
#    print(a.second)
#    print(a.microsecond)
    print(convert_time_to_index(a, fps))

#    print(vid.get_meta_data())
#    print(vid.get_length())


if __name__ == '__main__':
    main()

