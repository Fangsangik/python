"""
PyPi 배포
PyPI, build, package deploy
"""

# 완성된 패키지 불러오기
from my_package_02 import GifConverter as gfc

# 클래스 생성
c = gfc("./project/images/*png", "./project/image_out/animated.gif")

# 실행
c.convert_gif()

"""
package deploy 순서 
1. https://pypi.org/ 에 회원가입
2. 프로젝트 구조 확인
3. __init__.py 작성
4. 프로젝트 루트 필수 파일 작성 
    - Readme.md 작성
    - setup.py
    - setup.cfg
    - LICENSE
    - MANIFEST.in

5. pip install setuptools wheel -> 배포용 패키지 생성 
    - 설치 1 (가상환경) : python -m pip install --upgrade setuptools wheel
    - 설치 2 : python -m pip install --user --upgrade setuptools wheel
    - 빌드 : python setup.py sdist (sdist 파일이 형성된다)

6. PyPI 배포용 패키지 업로드
    - pip install twine
    - python -m twine upload dist/*
    - (testpypi) python -m twine upload --repository testpypi dist/*
    
7. 설치 확인 
    - pip install <패키지명>
    - from <패키지명> import <클래스명> as <별칭>
    
`setup.py`는 패키지의 이름, 버전, 설명, 필요한 의존성 등 메타데이터를 정의. 
배포 도구가 이 파일을 읽어 패키지를 빌드
"""


