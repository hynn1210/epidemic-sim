# ============================================================
# app.py — Streamlit 시연 화면  (실행: streamlit run app.py)
# ============================================================
# [공통] 둘이 함께 쓰는 파일.
#   - 충돌을 막기 위해 화면을 "구역별 함수"로 나누고, 각자 자기 함수만 수정한다.
#   - main()의 배치 순서를 바꿀 때는 상의한다.

import time

import matplotlib.pyplot as plt
import streamlit as st

from src.config import DEFAULT_PARAMS, PRESETS
from src.network import make_network
from src.monte_carlo import run_monte_carlo, compare_conditions
from src.analysis import summarize, compare_summary
from src.plot_curves import plot_sird, plot_compare, plot_counts_until
from src.plot_network import compute_layout, draw_day
from src.tracing import infection_generations


# ------------------------------------------------------------
# [A] 사이드바: 입력 슬라이더 + 시나리오 프리셋
# ------------------------------------------------------------
def draw_sidebar():
    """
    사용자 입력을 받아 params 딕셔너리로 돌려준다.
    반환: DEFAULT_PARAMS와 같은 키를 가진 딕셔너리
    """
    # TODO [A] st.sidebar 슬라이더: 인구 수, 슈퍼전파자 수, 전염률, 회복 기간, 치사율,
    #          초기 감염자 수, 반복 횟수, 병상 수, 격리 on/off, 추적 깊이, 확진까지 일수
    # TODO [A] 시나리오 프리셋 선택 (PRESETS 사용)
    # TODO [A] seed 입력칸
    pass


# ------------------------------------------------------------
# [A] S·I·R·D 곡선 영역
# ------------------------------------------------------------
def draw_curves(mc_result, beds):
    """몬테카를로 결과로 S·I·R·D 곡선을 보여 준다."""
    # TODO [A] plot_sird()로 그림 만들어 st.pyplot()으로 표시
    pass


# ------------------------------------------------------------
# [B] 요약 수치 + 의료 과부하 경고
# ------------------------------------------------------------
def draw_summary(summary):
    """summarize() 결과를 숫자 카드로 보여 주고, 병상 초과면 경고한다."""
    # TODO [B] st.metric()으로 정점 시점, 최대 감염자, 사망자 수 등 표시
    # TODO [B] summary["overload"]가 True면 st.warning()으로 의료 과부하 경고
    pass


# ------------------------------------------------------------
# [B] 노드 확산 탭 — 확산 과정을 동적으로 보여 주는 화면
# ------------------------------------------------------------
# 시뮬레이션은 이미 끝났고 매일의 상태가 result["history"]에 기록되어 있다.
# 이 기록을 하루씩 다시 그려서 "퍼져 나가는 모습"을 보여 준다.
def draw_network_tab(graph, result):
    """
    날짜 슬라이더(멈춰 보기)와 재생 버튼(자동으로 퍼지는 모습)으로 확산 과정을 보여 준다.
    result: simulate() 결과 1개 (예: mc_result["runs"][0])
    """
    # TODO [B] compute_layout()으로 위치 계산 (한 번만)
    # TODO [B] 그림이 들어갈 빈자리 만들기: st.empty()
    #
    # --- 날짜 슬라이더 (멈춰 보기) ---
    # TODO [B] st.slider로 날짜 선택 → draw_day(graph, pos, result["history"][날짜], result["sources"])
    #          → 빈자리에 표시
    #
    # --- 재생 버튼 (자동 재생) ---
    # TODO [B] st.button("재생")을 누르면 0일부터 마지막 날까지 반복:
    #            draw_day()로 그 날 그림 → 빈자리에 덮어쓰기 → plt.close(fig) → time.sleep(0.3)
    #
    # --- (선택) 곡선도 같이 움직이기 ---
    # TODO [B, 선택] 노드 그림 옆에 plot_counts_until(result["counts"], 날짜)로
    #          그날까지의 곡선을 함께 표시 (st.columns로 두 칸 나누기)
    #
    # --- (선택) 감염 세대 ---
    # TODO [B, 선택] infection_generations()로 "세대별 감염자 수"를 표나 숫자로 표시
    pass


# ------------------------------------------------------------
# [B] 격리 전후 비교 탭
# ------------------------------------------------------------
def draw_quarantine_compare(graph, params):
    """격리 없음 / 1단계 / 2단계 결과를 나란히 비교한다."""
    # TODO [B] compare_conditions() → plot_compare() + compare_summary() 표
    pass


# ------------------------------------------------------------
# [공통] 화면 조립
# ------------------------------------------------------------
def main():
    st.title("전염병 확산 시뮬레이터")
    # TODO [공통] 아래 순서로 조립
    #   1. params = draw_sidebar()
    #   2. graph = make_network(...) → mc_result = run_monte_carlo(...)
    #   3. draw_curves(), draw_summary(summarize(...))
    #   4. st.tabs(["노드 확산", "격리 비교"]) → draw_network_tab(), draw_quarantine_compare()
    pass


main()
