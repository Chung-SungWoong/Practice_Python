"""
qr코드 생성기
"""

import qrcode
"""
qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path = '4.QR코드 생성기\\' + qr_data + '.png'
qr_img.save(save_path)
"""
# txt파일에서 한 줄씩 읽어 qr코드를 생성하는 코드

file_path = r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/무제.rtf'
with open(file_path, 'rt',encoding='UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = '/Users/chung_sungwoong/Desktop/Practice/Practice_Python/' + qr_data + '.png'
        qr_img.save(save_path)