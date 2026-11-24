# ============================================================
# fake_data.py — 가짜 시뮬레이션 결과                  담당: [공통]
# ============================================================
# 진짜 simulate()가 완성되기 전에도 각자 시각화·분석을 개발할 수 있게 해 주는 가짜 데이터.

import networkx as nx

from src.config import S, I, R, D, Q


def make_fake_graph():
    """사람 10~20명 정도의 작은 그래프를 만든다."""
    # TODO [공통]
    pass


def make_fake_result():
    """
    simulate()의 반환 형식과 똑같은 모양의 가짜 결과를 만든다.
    반환: {"counts": ..., "history": ..., "infected_by": ..., "sources": ...}
    """
    # TODO [공통] 날짜 5~10일 정도, 상태가 S → I → R/D 로 자연스럽게 바뀌도록 직접 적기
    # TODO [공통] 진짜 simulate()가 나오면 진짜 결과로 바꿔서 확인하기
    pass
