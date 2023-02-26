# coding: utf-8
# cx_Freeze 用セットアップファイル
 
import sys
from cx_Freeze import setup, Executable
 
base = None

# GUI=有効, CUI=無効 にする
if sys.platform == 'win32' : base = 'Win32GUI'
 
# exe にしたい python ファイルを指定
exe = Executable(script = 'cct.py',
                 base = base)
 
# セットアップ
setup(name = 'cct',
      version = '0.1',
      description = 'chromecasttest',
      executables = [exe])