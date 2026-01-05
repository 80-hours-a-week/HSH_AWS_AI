class MessageGenerator:
  def __init__(self, monster_conquest_instance: int):
    self.mc = monster_conquest_instance
    self.messages = [
      "몬스터를 토벌합니다!",  # 0
      "몬스터의 초기 체력: {monster_hp}", # 1
      "\n현재 몬스터 체력: {monster_hp}", # 2
      "사용할 스킬을 선택하세요:", # 3
      "1. 화염 (데미지: 300)", # 4
      "2. 물   (데미지: 200)", # 5
      "3. 풀   (데미지: 100)", # 6
      "스킬 번호 입력 (1/2/3): ", # 7
      "몬스터에게 {damage}의 데미지를 입혔다. (남은 체력: {monster_hp})", # 8
      "몬스터가 반격했다. 그러나 아무 일도 없었다.", # 9
      "몬스터 처치 완료!" # 10
    ]

  def initial_messages(self: int):
    yield self.messages[0]
    yield self.messages[1].format(monster_hp=self.mc.monster_hp)

  def turn_start_messages(self: int):
    yield self.messages[2].format(monster_hp=self.mc.monster_hp)
    yield self.messages[3]
    yield self.messages[4]
    yield self.messages[5]
    yield self.messages[6]

  def input_prompt_message(self: int):
    yield self.messages[7]

  def damage_report_message(self: int, damage_dealt: int):
    yield self.messages[8].format(damage=damage_dealt, monster_hp=self.mc.monster_hp)

  def counter_attack_message(self: int):
    yield self.messages[9]

  def victory_message(self: int):
    yield self.messages[10]