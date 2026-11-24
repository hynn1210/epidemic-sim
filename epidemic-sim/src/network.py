# ============================================================
# network.py — 접촉 네트워크(그래프) 생성             담당: [A]
# ============================================================
# 노드 = 사람, 간선 = 서로 접촉하는 관계

import networkx as nx

from src.config import NETWORK_RANDOM, NETWORK_HUB, AVG_DEGREE, HUB_M


# ------------------------------------------------------------
# [A] 무작위형 네트워크
# ------------------------------------------------------------
def make_random_network(population, avg_degree, seed=None):
    """
    모든 사람의 친구 수가 비슷한 네트워크를 만든다.
    반환: networkx 그래프
    """
    # TODO [A] nx.erdos_renyi_graph 사용
    # TODO [A] 평균 친구 수가 나오도록 연결 확률 = avg_degree / (population - 1)
    pass


# ------------------------------------------------------------
# [A] 허브형 네트워크
# ------------------------------------------------------------
def make_hub_network(population, hub_m, seed=None):
    """
    친구가 아주 많은 소수(허브)가 있는 네트워크를 만든다.
    hub_m: 새 사람이 연결하는 친구 수
    반환: networkx 그래프
    """
    # TODO [A] nx.barabasi_albert_graph 사용
    pass


# ------------------------------------------------------------
# [A] 종류에 맞게 골라 주기 (app.py, 실험 노트북에서 사용)
# ------------------------------------------------------------
def make_network(network_kind, population, seed=None):
    """
    network_kind가 NETWORK_RANDOM이면 무작위형, NETWORK_HUB이면 허브형을 만든다.
    네트워크 모양 값은 config.py의 AVG_DEGREE, HUB_M을 쓴다.
    반환: networkx 그래프
    """
    # TODO [A]
    pass


# ------------------------------------------------------------
# [A, 선택] 완전 혼합 네트워크 — 이론 비교를 할 때만 필요
# ------------------------------------------------------------
def make_complete_network(population):
    """모두가 서로 연결된 네트워크를 만든다."""
    # TODO [A, 선택] nx.complete_graph 사용
    pass
