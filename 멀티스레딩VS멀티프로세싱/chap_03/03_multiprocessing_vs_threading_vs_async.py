"""
CPU Bound
- Process 진행이 CPU 속도에 의해 제한 결정 -> 행렬 곱, 고속된 연산, 압출 파일, 집합 연산 작업
- CPU 연산 위주 작업

I/O Bound
- 파일 쓰기, 디스크 작업, 네트워크 통신, 시리얼 포트 송수신 -> 작업에 의해 병목(수행시간)이 결정
- CPU 성능 지표가 수행시간 단축으로 크게 영향을 끼치지 않음

메모리 바인딩, 캐시 바인딩
-> 작업 목족에 따라서, 적절한 동시성 라이브러리 선택이 중요!

최종 비교
- 멀티 프로세싱 : 고가용성 CPU, utilization -> CPU BOUND -> 100% 활용 (10개 부엌, 10명 요리사, 10개 요리)
- Threading : Single(Multi) process, Multi Thread, os decides task switching -> feat I/O BOUND
   - 1개 부엌, 10명의 요리사, 10개 요리
- Asyncio : Single process, Single thread, cooperative multiTasking, tasks cooperatively decide switching
    -> slow I/O BOUND (1개 부엌, 1명의 요리사, 10개 요리)

동시성 라이브러리 비교
"""