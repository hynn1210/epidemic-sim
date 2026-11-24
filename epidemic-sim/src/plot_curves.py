# ============================================================
# plot_curves.py — S·I·R·D 곡선 그래프                 담당: [A]
# ============================================================
# 모든 그림 함수는 matplotlib의 fig를 돌려준다.
#   → app.py에서는 st.pyplot(fig), 보고서용은 save_figure(fig, 파일명)

import os

import matplotlib.pyplot as plt

from src.config import STATES, STATE_COLORS, I, RESULTS_DIR


# ------------------------------------------------------------
# [A] S·I·R·D 곡선
# ------------------------------------------------------------
def plot_sird(mc_result, beds=None, title=""):
    """
    run_monte_carlo() 결과로 날짜별 상태별 평균 곡선을 그린다.
    반환: fig
    """
    # TODO [A] 상태마다 mc_result["mean"] 곡선 그리기 (색은 STATE_COLORS)
    # TODO [A] mc_result["min"]~["max"] 범위를 옅은 색으로 칠하기 (fill_between)
    # TODO [A] beds가 있으면 가로 점선으로 표시
    pass


# ------------------------------------------------------------
# [A] 조건별 비교 그래프
# ------------------------------------------------------------
def plot_compare(results, state=I, beds=None, title=""):
    """
    compare_conditions() 결과에서 한 상태(기본: 감염자)의 곡선을 조건별로 겹쳐 그린다.
    감염병 특성별 비교, 격리 전후 비교에 같이 사용.
    반환: fig
    """
    # TODO [A] 조건 이름을 범례(legend)로 표시
    pass


# ------------------------------------------------------------
# [A] 그림 저장 (B도 같이 사용 가능)
# ------------------------------------------------------------
def save_figure(fig, filename):
    """fig를 results/filename 으로 저장한다."""
    # TODO [A] RESULTS_DIR 폴더에 저장 (폴더가 없으면 만들기)
    pass


# ------------------------------------------------------------
# [A, 선택] 이론 곡선 겹쳐 그리기 — 시간이 남으면
# ------------------------------------------------------------
def plot_with_theory(mc_result, theory_result, title=""):
    """시뮬레이션 평균 곡선 위에 theory.py의 곡선을 점선으로 겹쳐 그린다. 반환: fig"""
    # TODO [A, 선택]
    pass
