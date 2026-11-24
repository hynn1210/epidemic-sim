# ============================================================
# monte_carlo.py — 여러 번 반복해서 평균과 범위 구하기    담당: [B]
# ============================================================
# 한 번 실행한 결과는 운에 따라 달라지므로, 비교 실험은 모두 이 파일의 결과로 한다.
#
# params 규칙: config.DEFAULT_PARAMS와 같은 키 이름을 쓰는 딕셔너리.
#              그중 SIM_KEYS에 있는 것만 골라 simulate()에 넘긴다.

import copy

import numpy as np

from src.config import STATES, SIM_KEYS
from src.simulation import simulate


# ------------------------------------------------------------
# [B] 반복 실행
# ------------------------------------------------------------
def run_monte_carlo(graph, params, n_runs, seed=None):
    """
    simulate()를 n_runs번 반복해 날짜별 평균·최소·최대를 계산한다.
    반환 (이 모양은 확정, 바꿀 때 상의):
    {
      "mean": {S: [...], I: [...], ...},   # 날짜별 평균
      "min":  {S: [...], I: [...], ...},   # 날짜별 최소
      "max":  {S: [...], I: [...], ...},   # 날짜별 최대
      "runs": [simulate() 결과, ...],       # 각 실행 결과 (노드 그림용)
    }
    """
    # TODO [B] params에서 SIM_KEYS만 골라 simulate()에 넘기기
    # TODO [B] 실행마다 seed를 다르게 주기 (예: seed + 실행 번호) → 전체 결과는 재현 가능
    # TODO [B] align_lengths()로 길이 맞춘 뒤 numpy로 평균·최소·최대 계산
    pass


def align_lengths(counts_list):
    """
    실행마다 끝나는 날이 달라 리스트 길이가 다르므로,
    짧은 결과는 마지막 값으로 채워 가장 긴 길이에 맞춘다.
    입력: [각 실행의 counts, ...]   반환: 길이가 맞춰진 같은 모양의 리스트
    """
    # TODO [B]
    pass


# ------------------------------------------------------------
# [B] 조건별 비교
# ------------------------------------------------------------
def compare_conditions(graph, base_params, conditions, n_runs, seed=None):
    """
    여러 조건을 한 번에 실행해 결과를 조건 이름별로 묶는다.
    conditions 예:
      {"격리 없음": {"quarantine": False},
       "1단계":    {"quarantine": True, "trace_depth": 1},
       "2단계":    {"quarantine": True, "trace_depth": 2}}
    반환: {조건 이름: run_monte_carlo() 결과}
    ※ A의 "감염병 특성별 비교"에서도 이 함수를 같이 쓴다.
    """
    # TODO [B] base_params를 copy.deepcopy로 복사하고, 조건별로 바뀌는 값만 덮어쓰기
    # TODO [B] 모든 조건에 같은 seed를 줘서 공정하게 비교
    pass
