#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:42:21 2020

@author: philippe
"""
import os
import requests
from tqdm import tqdm

from bs4 import BeautifulSoup


def get_main_code(link, out_folder=''):
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')

    all_text = ''
    for code in soup.find_all('code', class_='sourceCode python'):
        for span in code.find_all('span', recursive=False):
            all_text += span.text + '\n'

    file_name = ''
    for strong in soup.find_all('strong'):
        tag_text = strong.text
        if tag_text.endswith('.py'):
            word_count = len(tag_text.split())
            if word_count == 1:
                file_name = tag_text
                break
    
    if len(file_name) == 0:
        print(f'No file reference in this at {link}')
        exit(0)

    print(f'Extracting fragments of {file_name}')
    with open(os.path.join(out_folder, file_name), 'w') as out_file:
        out_file.write(all_text)
    