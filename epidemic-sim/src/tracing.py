# ============================================================
# tracing.py — 접촉자 추적과 격리                     담당: [B]
# ============================================================
# 확산과 같은 BFS를 "찾아내기"에 응용한다. (발표 포인트)
# BFS는 networkx 함수를 쓰지 말고 collections.deque 로 직접 구현한다.
#
# simulation.py(A)는 이 파일의 quarantine_step()을 한 줄로 호출만 한다.
#   → quarantine_step의 이름, 인자, 반환값은 A와 약속한 것이므로 바꿀 때는 반드시 상의한다.
# ※ 이 파일은 simulation.py를 import 하지 않는다. (서로 import 하면 에러가 남)

from collections import deque

from src.config import S, I, Q


# ------------------------------------------------------------
# [B] 깊이 제한 BFS로 접촉자 찾기
# ------------------------------------------------------------
def trace_contacts(graph, confirmed_nodes, depth):
    """
    확진자들에서 깊이 제한 BFS를 해서 격리 대상 사람들을 찾는다.
    depth=1 → 확진자의 직접 접촉자, depth=2 → 접촉자의 접촉자까지.
    반환: 격리 대상 사람들의 집합(set)
    """
    # TODO [B] deque에 (사람, 깊이)를 넣고 시작 (확진자는 깊이 0)
    # TODO [B] 꺼낸 사람의 깊이가 depth보다 작을 때만 이웃을 큐에 추가
    # TODO [B] 이미 방문한 사람은 다시 넣지 않기 (visited 집합)
    # TODO [B] 확진자 본인 포함 여부는 아래 quarantine_step과 맞추기
    pass


# ------------------------------------------------------------
# [B] 확진 판단 + 격리: → Q  (simulation.py에서 매일 호출)
# ------------------------------------------------------------
def quarantine_step(graph, states, infected_day, day, confirm_delay, trace_depth):
    """
    감염 후 confirm_delay일이 지난 사람을 확진자로 보고,
    trace_contacts()로 접촉자를 찾아 Q로 바꾼다. (states를 직접 바꾼다)
    반환: 오늘 새로 격리된 사람 목록

    ※ A와의 약속: 이름, 인자, 반환값을 바꾸지 않는다.
       states / infected_day / day 의 의미는 simulation.py 맨 위 주석과 같다.
    """
    # TODO [B] 확진자 찾기: I이면서 (day - infected_day[사람]) == confirm_delay 인 사람
    # TODO [B] 확진자가 없으면 바로 빈 목록 반환 (추적 BFS를 부르지 않음)
    # TODO [B] trace_contacts(graph, 확진자들, trace_depth) 호출
    # TODO [B] 찾은 사람 중 S 또는 I인 사람을 Q로 전환 (R, D, 이미 Q인 사람은 그대로)
    #          접촉자는 실제 감염 여부를 따지지 않고 일단 격리한다
    #          격리는 해제하지 않는다 (끝까지 Q)
    # TODO [B] 확진자 본인도 Q로 바꿀지 첫날 함께 정하기
    pass


# ------------------------------------------------------------
# [B, 선택] 감염 세대(BFS 레벨) 계산
# ------------------------------------------------------------
# 감염 경로 트리는 제거했다. 이 함수는 "세대별 감염자 수"를 화면에 숫자로 보여 줄 때만 쓴다.
def infection_generations(infected_by, sources):
    """
    감염 경로에서 각 사람이 몇 세대 감염자인지 계산한다.
    최초 감염자 = 0세대, 그가 감염시킨 사람 = 1세대, ...
    반환: {사람: 세대 번호}
    """
    # TODO [B] infected_by(자식 → 부모)를 뒤집어 {부모: [자식들]} 만들기
    # TODO [B] sources에서 시작하는 BFS로 레벨 계산
    pass
