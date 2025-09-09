"""
애니메이션 변환
png, to gif, pil, image

package 작성
-> gif 이미지 변환기 -> package 호출 형태
"""

import glob  # 파일 경로를 쉽게 찾기 위한 모듈 -> LIST 형태로 반환
from PIL import Image  # 이미지 처리 모듈 파이썬 이미지 라이브러리
import logging


class GifConverter:
    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        """
        paht_in : 원본 이미지 경로(ex : imges/*.png)
        path_out : 저장할 이미지 경로 (ex : image_out/result.gif)
        resize : 리사이징 크기
        """
        self.path_in = path_in or "./project/images/*.png"
        self.path_out = path_out or "./image_out/result.gif"
        self.resize = resize

    def convert_gif(self):
        """
        GIF 이미지 변환
        :return:
        """
        logging.info(f"[GIF 변환 시작] {self.path_in} -> {self.path_out}")
        img, *imges = [Image.open(f).resize((self.resize), Image.LANCZOS) for f in sorted(glob.glob(self.path_in))]

        try:
            img.save(
                fp=self.path_out,  # 저장 경로
                format='GIF',  # 저장 포맷
                append_images=imges,  # 추가 이미지 리스트
                save_all=True,
                duration=100,
                loop=0
            )
            logging.info("[GIF 변환 완료]")

        except IOError as e:
            logging.error(f"[GIF 변환 실패] {e}")
            raise e
        return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    c = GifConverter("./project/images/*.png", "./image_out/result.gif", (320, 240))
    c.convert_gif()