
# 2장. 주변 친구

- `모바일 앱 기능을 지원`하는 `규모 확장이 용이`한 `백엔드 시스템 설계`
- 인근의 친구 목록을 보여주는 시스템
- 근접성 서비스와 유사해보일 수 있지만 주변 친구의 위치는 계속 바뀔 수 있음

## 1단계: 문제 이해 및 설계 범위 확정

- 주변? → 5마일(직선거리 기준)
- 10억명 유저 → DAU: 10% → 1억명
- 이동 이력 보관 → ML 등 다양한 용도로 활용 예정
- 10분 비활성화 시, 사라짐
- 이 단계에서 사생활 및 데이터 보호법은 고려 X