# ============================================================
# plot_network.py — 노드 확산 그림, 감염 경로 트리, GIF   담당: [B]
# ============================================================
# 모든 그림 함수는 matplotlib의 fig를 돌려준다.
#   → app.py에서는 st.pyplot(fig), 보고서용은 plot_curves.save_figure(fig, 파일명)

import os

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

from src.config import STATE_COLORS, RESULTS_DIR


# ------------------------------------------------------------
# [B] 노드 위치 고정
# ------------------------------------------------------------
def compute_layout(graph, seed=42):
    """
    노드 위치를 한 번만 계산한다. 이후 모든 그림에서 이 위치(pos)를 재사용한다.
    (매번 새로 계산하면 날짜마다 노드가 움직여서 비교가 안 됨)
    반환: pos = {사람: (x, y)}
    """
    # TODO [B] nx.spring_layout(graph, seed=seed)
    pass


# ------------------------------------------------------------
# [B] 특정 날짜의 노드 그림
# ------------------------------------------------------------
def draw_day(graph, pos, day_states, sources, title=""):
    """
    하루의 상태(history[날짜])로 노드를 색칠해 그린다.
    반환: fig
    """
    # TODO [B] day_states에 따라 STATE_COLORS로 색칠
    # TODO [B] 최초 감염자(sources)는 굵은 테두리
    # TODO [B] 허브형이면 친구 수(graph.degree)에 비례해 노드 크기 키우기
    pass


# ------------------------------------------------------------
# [B] 감염 경로 트리
# ------------------------------------------------------------
def draw_infection_tree(infected_by, generations, title=""):
    """
    누가 누구를 감염시켰는지 트리로 그린다.
    generations: tracing.infection_generations() 결과 → 세대별로 층을 나눠 배치
    반환: fig
    """
    # TODO [B] infected_by로 (부모 → 자식) 간선 만들기
    # TODO [B] 세대 번호를 y좌표로 써서 위에서 아래로 배치
    pass


# ------------------------------------------------------------
# [B] GIF 저장 (보고서용)
# ------------------------------------------------------------
def save_gif(graph, pos, history, sources, filename, interval=500):
    """
    날짜별 노드 그림을 이어 붙여 results/filename 으로 GIF를 저장한다.
    interval: 한 장면당 시간(밀리초)
    """
    # TODO [B] FuncAnimation으로 history를 하루씩 그리기
    # TODO [B] RESULTS_DIR 폴더에 저장 (writer="pillow")
    pass
