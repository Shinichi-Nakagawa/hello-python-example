# -*- coding: utf-8 -*-


# 他の人のプログラムを使うおまじない
from PIL import Image

# 自分のお名前を書く
__author__ = 'Shinichi Nakagawa'


# 画像で遊ぼう
def main(name):
    """
    画像を小さくして保存する
    :param name: 画像ファイルの名前
    :return:
    """
    # 画像を開く
    image = Image.open(name)
    # 画像の縦・横の半分のサイズを計算する
    thumbnail_size = (image.size[0] / 2, image.size[1] / 2)
    # 画像を半分にする
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)
    # 画像をファイルに保存する
    image.save('thumbnail.png')


if __name__ == '__main__':
    # 画像ファイルの名前
    main('python-logo-master-v3-TM.png')
