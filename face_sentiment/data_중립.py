import json
from PIL import Image

def open_json_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            # 파싱 성공시 데이터 리턴
            return json.load(file)
        except ValueError as e:
            print('파싱 실패! 에러 코드: {}'.format(e))
            # 파싱 성공시 None 리턴
            return None

def convert_bounding(size, box):
    dw = 1. / size[0] 
    dh = 1. / size[1]
    
    xmin = box["minX"]
    xmax = box["maxX"]
    ymin = box["minY"]
    ymax = box["maxY"]
    
    xmin = str(xmin*dw)
    xmax = str(xmax*dw)
    ymin = str(ymin*dh)
    ymax = str(ymax*dh)

    emo_class = str(0)
    
    return emo_class + ' ' + xmin + ' ' + xmax + ' ' + ymin + ' ' + ymax + '\n'
    #텍스트 파일에 추가할 문자 레이블


if __name__ == "__main__":
    json_data = open_json_file('img_emotion_validation_data(중립).json')

i = 0

while i < len(json_data):
    fname = json_data[0]["filename"]

    abox = json_data[0]["annot_A"]["boxes"]
    bbox = json_data[0]["annot_B"]["boxes"]
    cbox = json_data[0]["annot_C"]["boxes"]

    namelen = len(fname) - 4 #확장자 제거한 이름 길이
    tname = fname[:namelen] + '.txt'

    img = Image.open(fname)

    size = img.size
    result1 = convert_bounding(size, abox)
    result2 = convert_bounding(size, bbox)
    result3 = convert_bounding(size, cbox)

    f = open(tname, 'w')
    f.write(result1)
    f.write(result2)
    f.write(result3)
    f.close()

    i = i + 1


