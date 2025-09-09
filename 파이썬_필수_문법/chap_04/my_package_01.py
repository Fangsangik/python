"""
애니메이션 변환
png, to gif, pil, image

package 작성
-> 정적 이미지(JPG, PNG) => GIF 이미지 변환 패키지
"""

import glob # 파일 경로를 쉽게 찾기 위한 모듈 -> LIST 형태로 반환
from PIL import Image # 이미지 처리 모듈 파이썬 이미지 라이브러리

# 이미지 경로 생성
path_in = '/Users/hwangsang-ik/PythonLecture/파이썬_필수_문법/chap_04/project/images/*.png'# 원본 이미지 경로
path_out = '/Users/hwangsang-ik/PythonLecture/파이썬_필수_문법/chap_04/project/image_out/result.gif' # 저장할 이미지 경로

# 첫번째 이미지 & 모든 이미지 리스트 패킹
# 첫번쨰 이미지만 반영이 되고 나머지느 list
# img, *imges = [Image.open(f) for f in sorted(glob.glob(path_in))]

# 리사이즈 (필요한 경우)
img, *imges = [Image.open(f).resize((320, 240), Image.LANCZOS) for f in sorted(glob.glob(path_in))]


# 이미지 저장
img.save(
    fp = path_out, # 저장 경로
    format = 'GIF', # 저장 포맷
    append_images = imges, # 추가 이미지 리스트
    save_all= True,
    duration = 100,
    loop = 0
)
