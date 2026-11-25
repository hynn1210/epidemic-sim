# ============================================================
# network.py — 접촉 네트워크(그래프) 생성             담당: [A]
# ============================================================
# 노드 = 사람, 간선 = 서로 접촉하는 관계
# 네트워크는 한 종류만 쓴다: 무작위형 + 슈퍼전파자 몇 명
#   - 대부분의 사람은 친구 수가 AVG_DEGREE 근처로 비슷하다.
#   - 슈퍼전파자로 뽑힌 몇 명만 친구가 SUPERSPREADER_FRIENDS 명으로 아주 많다.
# 네트워크는 시뮬레이션 전에 한 번 만들고, 시뮬레이션 중에는 사람이 늘거나 줄지 않는다.

import random

import networkx as nx

from src.config import AVG_DEGREE, SUPERSPREADER_FRIENDS


# ------------------------------------------------------------
# [A] 기본 무작위형 네트워크
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
# [A] 슈퍼전파자 추가
# ------------------------------------------------------------
def add_superspreaders(graph, n_superspreaders, friends, seed=None):
    """
    그래프에서 n_superspreaders 명을 무작위로 골라, 각자 친구가 friends 명이 되도록
    다른 사람들과 새로 연결해 준다. (graph를 직접 바꾼다)
    반환: 슈퍼전파자로 뽑힌 사람 목록 (그림에서 표시하거나 확인할 때 사용)
    """
    # TODO [A] rng = random.Random(seed) 로 난수 생성기 만들기 (seed 고정 → 같은 사람이 뽑힘)
    # TODO [A] 슈퍼전파자를 n_superspreaders 명 무작위로 고르기
    # TODO [A] 각 슈퍼전파자마다, 아직 친구가 아닌 사람을 골라 graph.add_edge()로 연결
    #          → 친구 수(graph.degree)가 friends 가 될 때까지
    # 참고: 슈퍼전파자를 넣으면 전체 평균 친구 수가 조금 늘어난다 (보고서에 한 줄 적기)
    pass


# ------------------------------------------------------------
# [A] 최종 네트워크 만들기 (app.py, 실험 노트북에서 이것만 부르면 됨)
# ------------------------------------------------------------
def make_network(population, n_superspreaders, seed=None):
    """
    무작위형 네트워크를 만들고 슈퍼전파자를 n_superspreaders 명 추가한다.
    네트워크 모양 값은 config.py의 AVG_DEGREE, SUPERSPREADER_FRIENDS를 쓴다.
    n_superspreaders가 0이면 순수 무작위형이다.
    반환: networkx 그래프
    """
    # TODO [A] make_random_network() → add_superspreaders()
    pass


# ------------------------------------------------------------
# [A, 선택] 완전 혼합 네트워크 — 이론 비교를 할 때만 필요
# ------------------------------------------------------------
def make_complete_network(population):
    """모두가 서로 연결된 네트워크를 만든다."""
    # TODO [A, 선택] nx.complete_graph 사용
    pass
