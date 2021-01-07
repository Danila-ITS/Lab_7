#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит на экран все его
# предложения в обратном порядке.

if __name__ == '__main__':
    with open('txt.txt', 'r') as f:
        txt = f.read()
    print(txt)
    text = txt.split(" ")
    text.reverse()
    print(text)
