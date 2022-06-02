# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/CDHU Agentes/Desktop/bot_whatsapp/main.py'],
             pathex=['C:\\Users\\CDHU Agentes\\Desktop\\bot_whatsapp'],
             binaries=[],
             datas=[('C:/Users/CDHU Agentes/Desktop/bot_whatsapp/chrome', 'chrome/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='executavel',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='executavel')
