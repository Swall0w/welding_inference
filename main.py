import imageio
import pandas as pd
from datetime import datetime

def parse_time(timestamp):
    a = datetime.strptime(timestamp, '%M:%S.%f')
    return a

def main():
    videofile = 'data/output.mp4'
    txtfile = 'data/input.txt'

    dataframe = pd.read_csv(txtfile, delimiter='\t')
    time = dataframe['Weld Time'][1]
    print(time)
    a = parse_time(time)
    print(a.minute)
    print(a.second)
    print(a.microsecond)

    vid = imageio.get_reader(videofile, 'ffmpeg')
    fps = vid.get_meta_data()['fps']
    print(fps)
#    print(vid.get_meta_data())
#    print(vid.get_length())


if __name__ == '__main__':
    main()

