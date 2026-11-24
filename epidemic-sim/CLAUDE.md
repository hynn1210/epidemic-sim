# CLAUDE.md — 전염병 확산 시뮬레이터 (알고리즘 설계 팀 프로젝트)

이 파일은 Claude Code가 이 프로젝트를 이해하고 이어서 작업하기 위한 컨텍스트 문서다.
기획 단계에서 논의된 결정 사항, 아키텍처, 역할 분담, 할 일 목록을 담고 있다.

---

## 1. 프로젝트 개요

- **과목/성격**: 알고리즘 설계 수업 프로젝트. 알고리즘을 선택해 게임/서비스를 만드는 과제 (알고리즘 종류 제한 없음).
- **평가 기준**: **"해당 알고리즘을 구현해서 나온 데이터를 어떻게 활용할 것인가"**. → 엄밀한 이론 검증보다 **결과 데이터의 활용(비교 실험, 판단, 예측)**에 무게를 둔다.
- **팀**: 2인 (A, B). 둘 다 개발 경험이 적고 알고리즘에 익숙하지 않음 → **구현 난이도는 쉬움~중간**을 유지할 것.
- **주제**: 접촉 네트워크 위에서 감염병이 퍼지는 과정을 시뮬레이션하고, 사용자가 전염률·치사율 등을 조절해 확산 결과를 **예측**하는 시뮬레이터.
- **방향성**: "실제 현상을 검증"이 아니라 **"모델을 구현하고, 조건별 결과를 예측·비교해 활용한다"**.

### 주제 변경 이력
1. 처음에는 **소문 확산 시뮬레이션**(Maki-Thompson 모델, 무지자–전파자–억제자)으로 결정.
2. 이후 **전염병 확산 시뮬레이션(SIRD)**으로 변경. 구조(BFS + 상태 전이 + 몬테카를로)는 동일하게 유지.

---

## 2. 해결하려는 문제

감염병의 특성(전염률, 치사율, 회복 기간)과 대응(격리)에 따라 확산 결과가 크게 달라지지만 직관만으로는 예측하기 어렵다.
수치를 바꿔가며 결과(정점 시점, 최대 감염자, 사망자 수 등)를 미리 비교할 수 있는 도구를 만든다.

---

## 3. 사용 알고리즘과 모델 (확정)

| 알고리즘/모델 | 용도 |
|---|---|
| **BFS (확산)** | 감염자의 이웃을 큐로 탐색하며 전염률에 따라 감염시킴 (A 담당) |
| **BFS (추적)** | 확진자에서 깊이 제한(1~2단계) BFS로 접촉자를 찾아 격리 (B 담당) |
| **SIRD 모델 (+Q)** | 상태: S(비감염), I(감염), R(회복), D(사망), Q(격리) |
| **몬테카를로** | 확률적 결과를 여러 번 반복해 평균·범위 계산, 조건별 비교 (B 담당) |

- 격리 기능은 **새 알고리즘 없이 BFS 재사용**으로 구현한다. "하나의 알고리즘(BFS)을 두 문제(퍼뜨리기/찾아내기)에 응용"이 발표 포인트.
- 선택 사항: 연결 중심성(친구가 많은 사람 우선 격리). `networkx` 함수로 계산 가능. 필수 아님.

### 상태 전이 규칙
- S → I: 감염자(I)의 이웃이 S이면 전염률 `beta` 확률로 감염.
- I → R / D: 감염 후 `recovery_days`가 지나면 치사율 `fatality` 확률로 D, 아니면 R.
- 확진 → Q: 감염 후 `confirm_delay`일이 지나면 확진, 확진자 기준 추적 BFS로 접촉자를 Q로 전환. Q는 감염시키지도, 감염되지도 않음(확산 BFS에서 건너뜀).
- 종료: 감염자(I)가 0명이 되면 유행 종료로 판단.

### 프로그램 차원의 판단 (계획서의 "판단" 항목)
- 개인 단위: 감염 여부, 회복/사망 여부, 격리 대상 여부.
- 전체 단위: 감염 정점이 병상 수를 넘는지(의료 과부하 경고), 격리 1단계 vs 2단계 등 대응 방안 중 어느 쪽이 피해를 더 줄이는지.

---

## 4. 입력 / 출력

**입력 (사용자가 조절)**: 인구 수, 네트워크 종류(무작위형/허브형), 전염률, 회복 기간, 치사율, 초기 감염자 수, 반복 횟수, (선택) 병상 수, 격리 on/off 및 추적 깊이.
시나리오 프리셋 버튼(예: "독감형", "고치사형")으로 값을 한 번에 설정할 수 있게 한다.

**초기 상태**: 초기 감염자 몇 명, 나머지 전부 S.

**출력**:
- 단계별 S·I·R·D(·Q) 인원 그래프 (몬테카를로 평균 + 범위 음영)
- 감염 정점 시점, 최대 감염자 수, 최종 누적 감염률, 사망자 수, 유행 종료까지 걸린 기간
- 노드 확산 시각화(단계별 색), 감염 경로 트리, 감염 세대(BFS 레벨)
- 격리 전후 비교, 의료 과부하 여부

---

## 5. 검증 방법 (가볍게)

평가 기준이 "데이터 활용"이므로 이론 검증은 최소한으로 한다.

1. **임계값 확인 (필수)**: 감염자 1명이 평균 1명 미만을 감염시키는 조건에서 유행이 퍼지지 못하고 사그라드는지 확인.
2. **재현성 확인 (필수)**: 같은 `seed`면 같은 결과가 나오는지 확인.
3. **이론 비교 (선택, 우선순위 마지막)**: 완전 혼합 네트워크에서 몬테카를로 평균 곡선과 SIR 미분방정식 곡선 비교.
   - 하게 되면 `scipy` 대신 **오일러 방법(하루씩 더해 가는 `for` 반복문)**으로 단순하게 구현.
   - 시뮬레이션은 "정확히 며칠 뒤 회복", 방정식은 "매일 일정 비율 회복"이라 곡선이 완전히 같지는 않음 → 추세·정점 시점이 비슷한지만 본다.
4. **한계 명시**: 연령, 잠복기, 백신 등은 단순화했다고 보고서에 명시.

---

## 6. 결과 활용 (평가 핵심)

각 활용 주제를 **질문 → 몬테카를로 실험 → 결론** 형식으로 정리한다. 숫자는 반드시 몬테카를로 평균과 범위로 제시한다.
(예: "병상 50개인 학교에서 격리를 하면 과부하를 피할 수 있나?" → 비교 실험 → "2단계 격리 시 정점이 N% 낮아져 병상 이하 유지")

| 활용 주제 | 담당 |
|---|---|
| 감염병 특성별 비교: 고전염·저치사 vs 저전염·고치사 피해 양상 | A |
| 의료 자원 계획: 병상 수 대비 최대 감염자 수·시점 예측 | A |
| 방역 정책 비교: 격리 없음 / 1단계 / 2단계에서 정점이 얼마나 낮아지고 늦춰지는지 | B |
| 네트워크 구조 비교: 무작위형 vs 허브형 확산 속도·규모 | B |

추가 활용 포인트(보고서용): 교육용 도구("곡선을 평평하게" 체감), 학교·기관 대비(소규모 집단 확진자 발생 시 확산 규모 예측).

---

## 7. 개발 환경

- **에디터**: VS Code
- **언어**: Python
- **라이브러리**: `networkx`, `matplotlib`, `numpy`, `streamlit` (`scipy`는 이론 비교를 할 경우에만 선택)
- **확인 방식**: 개발 중 Jupyter 노트북 → 보고서용 그림은 `results/`에 파일 저장 → 발표 시연은 Streamlit (`streamlit run app.py`)
- 가상환경: `python -m venv venv` → 활성화 → `pip install -r requirements.txt`

### 협업 규칙 (Git)
- GitHub 저장소, 각자 브랜치에서 작업 후 `main`에 병합.
- **자주 병합한다**: 기능 하나가 끝날 때마다, 늦어도 2~3일에 한 번. 마감 직전 한꺼번에 병합하지 않는다.
- 작업 시작 전에 항상 `git pull`로 최신 `main`을 받는다.
- **파일 소유권을 지킨다**: 자기 담당 파일만 수정. 남의 파일을 고쳐야 하면 먼저 상대에게 말한다.
- 노트북(`.ipynb`)은 병합 충돌이 어려우므로 사람별로 따로 쓴다.
- 병합 후 `tests/test_basic.py`를 실행해 깨진 곳이 없는지 확인한다.

---

## 8. 파일 구조

```
epidemic-sim/
├── README.md               # [공통] 실행 방법, 팀 소개
├── CLAUDE.md
├── requirements.txt        # [공통]
├── .gitignore              # [공통] venv/, __pycache__/, .ipynb_checkpoints/
├── app.py                  # Streamlit 시연 화면 (구역별 함수로 나눠 A/B가 각자 자기 함수만 수정)
│
├── src/
│   ├── __init__.py
│   ├── config.py           # [공통] 상태 이름(S,I,R,D,Q), 색상, 기본 파라미터, 시나리오 프리셋 값
│   ├── network.py          # [A] 무작위형/허브형 네트워크 생성
│   ├── simulation.py       # [공통] 구역별 담당: 반복문 뼈대·기록[공통], 확산·회복/사망[A], 확진·격리[B]
│   ├── theory.py           # [A, 선택] SIR 미분방정식 (오일러 방법)
│   ├── tracing.py          # [B] trace_contacts() 추적 BFS, infection_generations() 감염 세대
│   ├── monte_carlo.py      # [B] 반복 실행, 평균·범위, 조건별 비교
│   ├── analysis.py         # [B] 정점 시점, 최종 감염률, 병상 초과 판단
│   ├── plot_curves.py      # [A] S·I·R·D 곡선 (+ 범위 음영, 이론 곡선은 선택)
│   └── plot_network.py     # [B] 노드 확산 그림, 감염 경로 트리, GIF
│
├── notebooks/
│   ├── A_dev.ipynb         # [A] 개인 실험용
│   ├── B_dev.ipynb         # [B] 개인 실험용
│   └── experiments.ipynb   # [공통] 보고서용 활용 실험 모음
│
├── conftest.py             # [공통] 비어 있는 pytest 설정 (tests에서 src import 가능하게)
├── tests/
│   ├── test_basic.py       # [공통] 임계값 테스트, seed 재현성 확인
│   └── fake_data.py        # [공통] 합의한 반환 형식의 가짜 결과 (진짜 엔진 완성 전 개발용)
│
├── results/                # 보고서용 그림, GIF (자동 저장)
└── docs/                   # 계획서, 보고서, 발표 자료
```

---

## 9. 역할 분담 (확정)

일의 성격: **A는 어렵고 핵심적인 일이 적게, B는 중간 난이도의 일이 많게.** 영역별(알고리즘·상태 전이·분석·시각화·활용)로 양쪽이 한 몫씩 맡는다.

| 구분 | A (확산과 특성 분석) | B (추적과 정책 비교) |
|---|---|---|
| BFS 응용 | 확산 BFS (S→I) | 추적 BFS (깊이 제한) + 감염 세대(BFS 레벨) |
| 상태 전이 | I→R/D (`simulation.py`의 [A] 구역) | 확진 판단 → Q 전환 (`simulation.py`의 [B] 구역) |
| 핵심 구조 | 확산 단계 구현 | 몬테카를로 반복, 평균·범위 계산 |
| 판단·분석 | 임계값 실험, (선택) 이론 비교 | 정점·감염률·병상 초과 판단 (`analysis.py`) |
| 활용 실험 | 감염병 특성별 비교, 의료 자원 계획 | 방역 정책 비교, 네트워크 구조 비교 |
| 시각화 | S·I·R·D 곡선 그래프 | 노드 확산 그림, 감염 경로 트리, GIF |
| 화면(`app.py`) | 사이드바 슬라이더, 시나리오 프리셋, 곡선 영역 | 날짜 슬라이더 + 노드 그림 탭, 과부하 경고, 격리 전후 비교 |
| 파일 | `network.py`, `plot_curves.py`, (`theory.py`) + `simulation.py`의 [A] 구역 | `tracing.py`, `monte_carlo.py`, `analysis.py`, `plot_network.py` + `simulation.py`의 [B] 구역 |

**공통**: 첫날 최소 버전 `simulate()` 함께 구현, `simulation.py`의 반복문 뼈대·하루 기록, `config.py`·인터페이스·가짜 데이터 합의, 테스트, 활용 실험 노트북, 계획서·보고서·발표.

### `simulation.py` 소유권 (공통 파일, 구역별 담당)
- 파일은 함께 쓰되 **구역별로 주인이 있다**: 반복문 뼈대·하루 기록·반환 형식 [공통], 확산·회복/사망 [A], 확진 판단·격리 [B].
- 자기 구역만 수정한다. [공통] 구역은 바꿀 때 반드시 상의한다.
- 기능 하나를 끝낼 때마다 `main`에 병합하고, 병합 후 `tests/test_basic.py`를 실행한다.
- 첫날 함께 만든 최소 버전(S→I + I→R) 덕분에 B는 첫날부터 진짜 결과로 작업할 수 있다.
- **해 보고 너무 비효율적이면 파일 전체를 A 담당으로 옮긴다.** 이때 B의 격리 구역은 `tracing.py`로 옮기고 `simulation.py`는 호출만 한다.

### 한쪽이 밀릴 때 넘길 수 있는 일
- **A가 밀릴 때 → B에게**: 임계값 실험, 곡선 그래프의 몬테카를로 범위 음영.
- **B가 밀릴 때 → A에게**: 네트워크 구조 비교 실험, 과부하 경고 화면.

---

## 10. 모듈 간 인터페이스

**실제 함수 이름·인자·반환 형식은 각 파일의 뼈대(`def` + docstring)가 기준이다.** 아래는 요약이다.
이름을 바꿀 때는 상의하고, 뼈대와 이 절을 함께 고친다.

### 이름 규칙 (`src/config.py`에 정의)
- 상태: `S, I, R, D, Q`, 목록 `STATES`, 색 `STATE_COLORS`
- 네트워크 종류: `NETWORK_RANDOM = "random"`, `NETWORK_HUB = "hub"`
- 파라미터 딕셔너리 `params`의 키는 `DEFAULT_PARAMS`의 키를 그대로 쓴다:
  `population, network_kind, beta, recovery_days, fatality, initial_infected, quarantine, trace_depth, confirm_delay, n_runs, beds, seed`
- 그중 `simulate()`에 넘기는 키는 `SIM_KEYS` (= `simulate()`의 인자 이름과 같음)
- 시뮬레이션 공용 변수: `states`, `infected_day`, `infected_by`, `day`, `rng`(= `random.Random(seed)`, 난수는 반드시 `rng`로만)

### 주요 함수 (파일별)
- `network.py` [A]: `make_random_network`, `make_hub_network`, `make_network`, (선택) `make_complete_network`
- `simulation.py`: `simulate`, `record_day` [공통] / `spread_step`, `progress_step` [A] / `quarantine_step` [B]
- `tracing.py` [B]: `trace_contacts`, `infection_generations`
- `monte_carlo.py` [B]: `run_monte_carlo(graph, params, n_runs, seed)` → `{"mean","min","max","runs"}`, `align_lengths`, `compare_conditions(graph, base_params, conditions, n_runs, seed)`
- `analysis.py` [B]: `summarize(counts, population, beds)` → `{"peak_day","peak_infected","attack_rate","deaths","duration","overload"}`, `overload_days`, `compare_summary`
- `plot_curves.py` [A]: `plot_sird`, `plot_compare`, `save_figure`, (선택) `plot_with_theory`
- `plot_network.py` [B]: `compute_layout`, `draw_day`, `draw_infection_tree`, `save_gif`
- `theory.py` [A, 선택]: `solve_sir_euler`
- `app.py`: `draw_sidebar`, `draw_curves` [A] / `draw_summary`, `draw_network_tab`, `draw_quarantine_compare` [B] / `main` [공통]
- 그림 함수는 모두 matplotlib `fig`를 반환한다 (Streamlit은 `st.pyplot(fig)`, 저장은 `save_figure`).

### 실행 경로 주의
- `streamlit run app.py`, `pytest`는 **프로젝트 맨 위 폴더에서** 실행한다 (`conftest.py`가 있어야 `from src...`가 동작).
- 노트북은 첫 칸에서 `sys.path.append("..")`를 해야 `src`를 불러올 수 있다.
- `tracing.py`는 `simulation.py`를 import 하지 않는다 (순환 import 방지).

### `simulate()` 요약

```python
# src/simulation.py ([공통], 구역별 담당)
def simulate(graph, beta, recovery_days, fatality, initial_infected,
             quarantine=False, trace_depth=1, confirm_delay=2, seed=None):   # [공통]
    """
    매일 반복:
        spread_step(...)        # [A] 확산 BFS (S→I)
        progress_step(...)      # [A] I→R/D
        if quarantine:
            quarantine_step(...)    # [B] 확진 판단 + 추적 BFS(tracing.py) + Q 전환
        record_day(...)         # [공통] 하루 기록
    I가 0명이 되면 종료.

    반환값:
    {
      "counts": {"S": [...], "I": [...], "R": [...], "D": [...], "Q": [...]},  # 단계별 인원 수
      "history": [ {node: state, ...}, ... ],                                # 단계별 노드 상태
      "infected_by": {node: parent_node, ...},                               # 감염 경로 (트리용)
      "sources": [...],                                                      # 최초 감염자
    }
    """

```

- 반환 형식과 상태 저장 방식이 바뀌면 반드시 상대에게 알리고 이 절을 갱신한다.
- 첫날 합의한 형식대로 **가짜 결과 데이터**(`tests/fake_data.py`)를 만들어 두면, 각자 상대 코드 없이도 개발·테스트할 수 있다.

---

## 11. 노드 시각화 방침

- `networkx` + `matplotlib`. **노드 위치(`spring_layout(seed=42)`)는 한 번만 계산해 고정**.
- 색: S=lightgray, I=red, R=green, D=black, Q=blue. 최초 감염자는 굵은 테두리. (`config.py`에 정의)
- 노드 수 100~300명 권장. 허브형은 연결 수에 비례해 노드 크기 조절.
- 출력 방식: GIF(`FuncAnimation`, 보고서용), Streamlit 날짜 슬라이더(시연용, 추천), pyvis(선택).

---

## 12. 할 일 목록

### 공통 (A + B)
**1단계: 준비 (첫날)**
- [ ] GitHub 저장소 생성, 8절 폴더 뼈대, `.gitignore`, `README.md`
- [ ] 가상환경 세팅, `requirements.txt`
- [ ] `config.py`: 상태 이름, 색상, 기본 파라미터, 시나리오 프리셋 값 합의
- [ ] 인터페이스 합의: `simulate()` 반환 형식, 상태 저장 방식, 각 단계 함수 입출력
- [ ] 합의한 형식대로 가짜 결과 데이터 만들기 (`tests/fake_data.py`)
- [ ] **최소 버전 `simulate()` 함께 구현** (`deque`로 확산 BFS, S→I + I→R까지)

**3단계: 통합**
- [ ] `simulate()`에서 격리 단계 켜고 함께 디버깅
- [ ] `simulation.py` 공동 작업이 비효율적인지 점검 → 그렇다면 A 담당으로 옮기기 (9절)
- [ ] `tests/test_basic.py`: seed 재현성, 임계값 조건 테스트

**4단계: 결과물**
- [ ] `experiments.ipynb`: 활용 실험 모아서 실행, 그림을 `results/`에 저장
- [ ] 계획서 (문제, 핵심 기능, 판단, 입력/초기 상태, 출력/상태 변화)
- [ ] 보고서 (활용 실험 결과, 검증, 한계점)
- [ ] 발표 자료 및 시연 리허설

### A (확산과 특성 분석)
- [ ] `network.py`: 무작위형(`erdos_renyi_graph`), 허브형(`barabasi_albert_graph`) 생성
- [ ] `simulation.py` [A] 구역: `spread_step()` 확산 BFS, Q 노드 건너뛰기
- [ ] `simulation.py` [A] 구역: `progress_step()` — 회복 기간 경과 시 치사율로 R/D 결정
- [ ] 임계값 실험
- [ ] `plot_curves.py`: S·I·R·D(·Q) 곡선, 몬테카를로 범위 음영
- [ ] `app.py`: 사이드바 슬라이더, 시나리오 프리셋 버튼, 곡선 영역
- [ ] 활용 실험: 감염병 특성별 비교, 의료 자원 계획(병상 수 대비 정점)
- [ ] (선택, 우선순위 마지막) `theory.py`: 오일러 방법 SIR 곡선과 비교

### B (추적과 정책 비교)
- [ ] 가짜 데이터로 노드 시각화 프로토타입
- [ ] `tracing.py`: `trace_contacts()` 깊이 제한 BFS (`deque` 직접 구현)
- [ ] `simulation.py` [B] 구역: `quarantine_step()` 확진 판단 → 추적 → Q 전환
- [ ] `tracing.py`: `infection_generations()` 감염 세대 계산
- [ ] `monte_carlo.py`: 반복 평균·최소·최대, 조건별 비교
- [ ] `analysis.py`: `summarize()` 정점 시점, 최종 감염률, 병상 초과 판단
- [ ] `plot_network.py`: 노드 확산 그림, 감염 경로 트리, GIF 저장
- [ ] `app.py`: 날짜 슬라이더 + 노드 그림 탭, 과부하 경고, 격리 전후 비교
- [ ] 활용 실험: 방역 정책 비교(격리 없음/1단계/2단계), 네트워크 구조 비교(무작위형/허브형)

---

## 13. 참고 자료

**고전 모델**
- Kermack & McKendrick (1927): SIR 모델의 원조.
- Daley & Kendall, "Epidemics and Rumours", Nature 204, 1118 (1964). https://doi.org/10.1038/2041118a0 (소문 주제 시절 기준 논문)
- Moreno, Nekovee, Pacheco, "Dynamics of Rumor Spreading in Complex Networks", Phys. Rev. E 69, 066130 (2004). https://arxiv.org/abs/cond-mat/0312131 (네트워크 위 몬테카를로 확산)
- Nekovee et al., "Theory of Rumour Spreading in Complex Social Networks" (2008). https://arxiv.org/abs/0807.1458 (허브형 네트워크가 더 빨리 퍼짐)

**실제 데이터 적용 사례 (근거 보강용)**
- "Using Epidemiological Models to Predict the Spread of Information on Twitter", Algorithms (MDPI, 2023). https://www.mdpi.com/1999-4893/16/8/391
- SNAP Higgs Twitter Dataset (리트윗 시각 포함, 선택 과제). https://snap.stanford.edu/data/higgs-twitter.html

---

## 14. Claude Code 작업 시 유의사항

- 팀원이 초보자이므로 **코드는 단순하고 주석이 충분하게**, 한 함수가 한 가지 일만 하도록 작성.
- 외부 라이브러리 함수로 BFS를 대체하지 말 것 (`nx.bfs_tree` 등 사용 금지). **BFS는 `collections.deque`로 직접 구현**해야 과제 의도에 맞음.
- 랜덤 결과 재현을 위해 `seed` 인자를 지원할 것.
- 담당(A/B) 경계를 지켜 파일을 수정하고(9절 소유권), 인터페이스 변경 시 이 문서의 10절을 갱신할 것.
- 평가 기준이 "데이터 활용"이므로, 기능 추가보다 **비교 실험과 판단 결과를 잘 보여 주는 쪽**을 우선할 것.
- **함수 안의 실제 구현은 팀원이 직접 짠다.** 뼈대(`import`, `def` + docstring, `pass`, `config.py`의 이름 정의)와 `# TODO [A]/[B]/[공통]` 주석까지만 Claude가 작성하고, 사용자가 명시적으로 요청하기 전까지 함수 본문은 채우지 말 것.
- 응답과 주석은 한국어로.
