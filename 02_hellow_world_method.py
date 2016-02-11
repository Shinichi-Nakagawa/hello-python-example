# -*- coding: utf-8 -*-

# 自分のお名前を書く
__author__ = 'Shinichi Nakagawa'


# 関数を使ってみよう
def main(name):
    # 挨拶をする
    print('Hellow, {name}!'.format(name=name))


if __name__ == '__main__':
    # 自分の名前を言ってみよう
    main(__author__)
