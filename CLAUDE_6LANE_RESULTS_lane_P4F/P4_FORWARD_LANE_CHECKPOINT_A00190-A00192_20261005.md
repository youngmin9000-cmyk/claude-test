# P4 FORWARD — lane_P4F checkpoint (A00190~A00192 완료)

- 작성: 2026-10-05, append-only. 이전 checkpoint는 `P4_FORWARD_LANE_CHECKPOINT_A00189_20261005.md`
- Drive 업로드: 하지 않음

## 마지막 완료 지점
- A00190 / A00192 / A00191 `[천재류] 확통 교사용 각종평가자료 (2).vol1/vol2/vol3.egg` (분할 EGG 하나의 소스)
  - vol1 sha256 5dc6c5bb…, vol2 86fbbfbb…, vol3 d2fa431f…
  - 자체 EGG 파서로 결합 추출: deflate, 29개 member CRC 전부 일치
  - 기초력up 13개: B075–B079 / 소단원평가 13개: B080–B087 / 대단원평가 3개: B088–B093
  - 문항ID prefix `D_5dc6c5bb76b7_P4FA00190_` (세 queue ID는 동일 소스이므로 A00190 대표)
  - source_new_build_complete = YES (A00190, A00191, A00192 모두)
  - repair_pending = YES (아래 REVIEW 8건)
- 수정 기록: B090은 같은 세션에서 처음 만들었을 때 validator error 1건(원문조건충돌이 있는데 YES)이 있었음. 해당 행을 REVIEW로 바꿔 같은 파일명으로 다시 만듦. 수정 전 버전은 git history에 남아 있음.

## 다음 미처리 지점
- A00263 `중2 수학 비상 문제자료(교사용).zip` (22MB, DUPLICATE_RECHECK)
- 그 다음 A00332 …

## 누적
| 구분 | 행 |
|---|---|
| 이전 B001–B039 | 670 |
| lane B040–B074 (A00189) | 417 |
| lane B075–B093 (A00190~92) | 196 |
| **누적 unique** | **1283** |
| REVIEW 누적 | 13 (이전 4 + A00189 QZ1A Q2 + A00190 8건) |
| HOLD | 0 |

## A00190 REVIEW (repair_pending)
| 문항ID | 사유 |
|---|---|
| GB11_Q004 | ⑶ '네 자리' 문제인데 해설은 세 자리로 계산(100). 독립풀이 500 |
| GB35_Q002 | 해설이 V(X̄)=σ²/√n 오공식. 독립풀이 9, 4, 9/4, 1 |
| SD21_Q003 | 원 8등분점 이등변삼각형 24개 중 16개만 셈. 독립풀이 3/7 (원답 2/7) |
| SD33_Q002 | 문제 B(196,p), 해설 B(144,p). 문제 기준 720/49 |
| BD2_Q001 | 합 9 경우 누락. 독립풀이 ④ 1/3 (원답 ②) |
| BD2_Q011 | 원문 P(A∩B)=3/4 불가능(∪ 오기). 해설 기준 ④ |
| BD3_Q010 | n·3ⁿ⁻¹=324인 자연수 없음(원답 ④) |
| BD3_Q012 | 최대 조건이 σ에 의존. 원해설 논리 오류(원답 ③) |

- PASS_WITH_DEFECT(YES): GB34_Q003. 정답란 0.9014 ↔ 해설 0.9104, 독립풀이 0.9104
