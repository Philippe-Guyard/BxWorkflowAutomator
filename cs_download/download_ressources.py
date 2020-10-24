#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:26:08 2020

@author: philippe
"""
import os

import requests
from tqdm import tqdm

from bs4 import BeautifulSoup


def get_txt_files(link, out_folder=''):
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')

    text_files = [x['href'] for x in soup.find_all('a') if x['href'].endswith('.txt')]
    for url in text_files:
        file_name = url.split('/')[-1]
        file = requests.get(url, stream=True)
        with open(os.path.join(out_folder, file_name), 'wb') as out_file:
            for data in tqdm(file.iter_content(), desc=f'Downloading {file_name}'):
                out_file.write(data)            

