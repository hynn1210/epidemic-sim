# ============================================================
# test_basic.py — 기본 테스트                         담당: [공통]
# ============================================================
# 실행: 프로젝트 맨 위 폴더에서  pytest
# main에 병합한 뒤에는 꼭 실행해서 깨진 곳이 없는지 확인한다.
# 아직 만들지 않은 테스트는 pytest.skip()으로 "건너뜀"이 표시된다. 구현하면 skip 줄을 지운다.

import networkx as nx
import pytest

from src.config import S, I, R, D, Q, STATES
from src.simulation import simulate, spread_step
from src.tracing import trace_contacts


# ------------------------------------------------------------
# [공통]
# ------------------------------------------------------------
def test_same_seed_same_result():
    """같은 seed로 두 번 실행하면 결과가 똑같아야 한다."""
    pytest.skip("TODO [공통]")


def test_low_beta_dies_out():
    """전염률이 아주 낮으면(감염자 1명이 평균 1명 미만 감염) 유행이 금방 사그라들어야 한다."""
    pytest.skip("TODO [공통]")


def test_population_conserved():
    """매일 S + I + R + D + Q 합이 인구 수와 같아야 한다."""
    pytest.skip("TODO [공통]")


# ------------------------------------------------------------
# [A]
# ------------------------------------------------------------
def test_spread_beta_zero():
    """전염률이 0이면 아무도 새로 감염되지 않아야 한다."""
    pytest.skip("TODO [A]")


def test_spread_beta_one():
    """전염률이 1이면 감염자의 이웃(S)이 모두 감염되어야 한다."""
    pytest.skip("TODO [A]")


# ------------------------------------------------------------
# [B]
# ------------------------------------------------------------
def test_trace_depth():
    """일렬로 연결된 5명(nx.path_graph(5))에서 깊이 1, 2일 때 찾는 사람이 맞아야 한다."""
    pytest.skip("TODO [B]")
