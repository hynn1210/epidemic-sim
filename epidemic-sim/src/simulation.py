# ============================================================
# simulation.py — 시뮬레이션 엔진                     담당: [공통] (구역별로 A / B)
# ============================================================
# 작업 규칙
#   1. 자기 구역의 함수만 수정한다. (서로 다른 줄을 고치므로 Git이 자동으로 병합해 준다)
#   2. [공통] 구역(simulate, record_day, 반환 형식)은 바꿀 때 반드시 상의한다.
#   3. 함수 이름과 인자 이름은 바꾸지 않는다. 바꿔야 하면 상의하고 CLAUDE.md 10절도 고친다.
#   4. 기능 하나를 끝낼 때마다 main에 병합하고, 작업 전에는 git pull 로 최신 코드를 받는다.
#   5. 병합한 뒤에는 pytest 로 tests/test_basic.py 를 실행해 깨진 곳이 없는지 확인한다.
#   ※ 해 보고 너무 비효율적이면 이 파일 전체를 A 담당으로 옮긴다.
#
# 함수들이 같이 쓰는 변수 (이름 확정)
#   states       = {사람: S/I/R/D/Q}       현재 각 사람의 상태
#   infected_day = {사람: 감염된 날짜}       회복·확진 시점 계산용
#   infected_by  = {사람: 감염시킨 사람}     감염 경로 트리용 (최초 감염자는 None)
#   day          = 오늘 날짜 (0부터 시작)
#   rng          = 난수 생성기 (random.Random(seed)). 난수는 반드시 rng로만 뽑는다 → 같은 seed면 같은 결과
#
# 주의: BFS는 networkx 함수(bfs_tree 등)를 쓰지 말고 collections.deque 로 직접 구현한다.

import random
from collections import deque

from src.config import S, I, R, D, Q, STATES
from src.tracing import trace_contacts


# ------------------------------------------------------------
# [공통] 반복문 뼈대 — 첫날 함께 만드는 최소 버전
# ------------------------------------------------------------
def simulate(graph, beta, recovery_days, fatality, initial_infected,
             quarantine=False, trace_depth=1, confirm_delay=2, seed=None):
    """
    감염병 확산을 하루 단위로 시뮬레이션한다.

    반환 (이 모양은 확정, 바꿀 때 상의):
    {
      "counts": {S: [...], I: [...], R: [...], D: [...], Q: [...]},  # 날짜별 상태별 인원 수
      "history": [ {사람: 상태, ...}, ... ],                       # 날짜별 모든 사람의 상태
      "infected_by": {사람: 감염시킨 사람, ...},                    # 감염 경로
      "sources": [...],                                            # 최초 감염자 목록
    }
    """
    # TODO [공통] rng = random.Random(seed) 만들기
    # TODO [공통] 모두 S로 시작, 초기 감염자를 rng로 무작위로 골라 I로 (sources에 저장)
    # TODO [공통] counts, history 빈 값으로 준비하고 0일째 기록
    # TODO [공통] I가 0명이 될 때까지 하루씩 반복
    #             spread_step → progress_step → (quarantine이면) quarantine_step → record_day
    # TODO [공통] 반환 딕셔너리 만들어 돌려주기
    pass


# ------------------------------------------------------------
# [공통] 하루 기록
# ------------------------------------------------------------
def record_day(states, counts, history):
    """오늘의 상태별 인원 수를 counts에, 모든 사람 상태의 복사본을 history에 추가한다."""
    # TODO [공통] STATES를 돌며 상태별 인원 세서 counts에 추가
    # TODO [공통] states를 "복사해서" history에 추가 (복사하지 않으면 모든 날이 같은 값이 됨)
    pass


# ------------------------------------------------------------
# [A] 확산: S → I  (확산 BFS)
# ------------------------------------------------------------
def spread_step(graph, states, infected_day, infected_by, day, beta, rng):
    """
    오늘의 감염자(I)에서 이웃을 살펴 S인 사람을 beta 확률로 I로 바꾼다.
    반환: 오늘 새로 감염된 사람 목록
    """
    # TODO [A] 오늘의 감염자를 deque에 넣고 하나씩 꺼내며 이웃 확인
    # TODO [A] 이웃이 S이면 rng.random() < beta 로 감염 판정
    #          → 성공하면 states를 I로, infected_day·infected_by 기록
    # TODO [A] Q인 사람은 감염시키지도, 감염되지도 않으므로 건너뛰기
    # TODO [A] 오늘 새로 감염된 사람은 내일부터 전파하게 하기 (같은 날 연쇄 감염 방지)
    pass


# ------------------------------------------------------------
# [A] 회복·사망: I → R / D
# ------------------------------------------------------------
def progress_step(states, infected_day, day, recovery_days, fatality, rng):
    """감염 후 recovery_days가 지난 I를 fatality 확률로 D, 아니면 R로 바꾼다."""
    # TODO [A] I인 사람 중 (day - infected_day[사람]) >= recovery_days 인 사람 찾기
    # TODO [A] rng.random() < fatality 이면 D, 아니면 R
    pass


# ------------------------------------------------------------
# [B] 확진 판단 + 격리: → Q
# ------------------------------------------------------------
def quarantine_step(graph, states, infected_day, day, confirm_delay, trace_depth):
    """
    감염 후 confirm_delay일이 지난 사람을 확진자로 보고,
    trace_contacts()로 접촉자를 찾아 Q로 바꾼다.
    반환: 오늘 새로 격리된 사람 목록
    """
    # TODO [B] 확진자 찾기: I이면서 (day - infected_day[사람]) == confirm_delay 인 사람
    # TODO [B] trace_contacts(graph, 확진자들, trace_depth) 호출
    # TODO [B] 찾은 사람 중 S 또는 I인 사람을 Q로 전환 (R, D는 그대로)
    # TODO [B] 확진자 본인도 Q로 바꿀지 첫날 함께 정하기
    pass
