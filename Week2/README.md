## 파일 구성

프로젝트는 기능별로 모듈화된 3개의 파일로 구성되어 있습니다.

- **`main.py`**: 게임의 진입점(Entry Point)입니다. `MonsterConquest` 클래스가 정의되어 있으며, `GameVariableData`를 상속받아 전반적인 전투 흐름(`fightprocess`)을 제어합니다. 또한 `asyncio`를 활용하여 몬스터의 주기적인 공격(`periodic_attack`)을 비동기적으로 처리합니다.
- **`GameVariableData.py`**: 게임의 데이터(몬스터 체력, 스킬 정보 등)를 관리하는 클래스가 정의되어 있습니다.
- **`MessageGenerator.py`**: 게임 진행 상황에 따른 텍스트 출력을 담당합니다. Python의 Generator(`yield`)를 사용하여 메시지를 순차적으로 반환합니다.

## 기술적 특징

- **상속(Inheritance)**: `MonsterConquest` 클래스는 `GameVariableData`를 상속받아 데이터와 로직을 연결합니다.
- **제너레이터(Generator)**: `MessageGenerator` 클래스는 `yield` 키워드를 사용하여 메모리를 효율적으로 사용하며 메시지를 생성합니다.
- **비동기 프로그래밍(Asynchronous Programming)**: `asyncio` 라이브러리를 사용하여 사용자의 입력을 기다리는 동안에도 몬스터가 주기적으로 공격하는 동시성 로직을 구현했습니다.
- **예외 처리**: 사용자가 정의되지 않은 스킬 번호를 입력할 경우 `KeyError`를 처리하여 안내 메시지를 출력하고 종료합니다.
