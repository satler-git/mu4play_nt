"""cct"""
import argparse
import sys
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

# パーサーを作る
parser = argparse.ArgumentParser(
            prog='cct', # プログラム名
            usage='pychromecast test', # プログラムの利用方法
            description='description', # 引数のヘルプの前に表示
            epilog='end', # 引数のヘルプの後で表示
            add_help=True, # -h/–help オプションの追加
            )
 
# 引数の追加
parser.add_argument('-l', '--list', help='Chromecast list', action="store_true")
parser.add_argument('-n', '--name', help='Chromecast\'s name')
parser.add_argument('-i', '--id', help='Video\'s id')
# 引数を解析する
args = parser.parse_args()


if args.list:
    #listup
    casts, browser = pychromecast.get_chromecasts()
    # Shut down discovery as we don't care about updates
    browser.stop_discovery()
    if len(casts) == 0:
        #長さが0の場合(クロームキャストがない)
        print("No Devices Found")
        sys.exit(1)

    print("Found cast devices:")
    for cast in casts:
        print(
            f'  "{cast.name}"with UUID:{cast.uuid}'  # pylint: disable=protected-access
        )
else:
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[args.name])
    if not chromecasts:
        #クロームキャストがない
        print(f'No chromecast with name "{args.name}" discovered')
        sys.exit(1)
    cast = chromecasts[0]
    # Start socket client's worker thread and wait for initial status update
    cast.wait()

    yt = YouTubeController()
    cast.register_handler(yt)
    yt.play_video(args.id)

    # Shut down discovery
    browser.stop_discovery()