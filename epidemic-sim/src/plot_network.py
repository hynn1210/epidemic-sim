# ============================================================
# plot_network.py — 노드 확산 그림                    담당: [B]
# ============================================================
# 모든 그림 함수는 matplotlib의 fig를 돌려준다.
#   → app.py에서는 st.pyplot(fig) 또는 재생용 빈자리(st.empty)에 표시
# 확산 과정은 app.py에서 날짜 슬라이더 + 재생 버튼으로 draw_day()를 하루씩 다시 그려서 보여 준다.

import matplotlib.pyplot as plt
import networkx as nx

from src.config import STATE_COLORS


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
    재생 버튼에서 하루씩 반복해서 부르므로, 그림 한 장만 만들고 돌려준다.
    반환: fig
    """
    # TODO [B] 친구 관계 선을 옅은 회색으로 (nx.draw_networkx_edges)
    # TODO [B] day_states에 따라 STATE_COLORS로 색 목록 만들어 점 그리기 (nx.draw_networkx_nodes)
    # TODO [B] 최초 감염자(sources)는 굵은 테두리
    # TODO [B] 친구 수(graph.degree)에 비례해 점 크기 키우기 → 슈퍼전파자가 눈에 띄게
    # TODO [B] 재생할 때 그림이 계속 쌓이지 않도록, 다 쓴 fig는 plt.close(fig)로 닫기 (app.py 쪽에서)
    pass
