from GameVariableData import *
from MessageGenerator import *
import asyncio

class MonsterConquest(GameVariableData):
  def __init__(self):
    super().__init__()
    self.msg_gen = MessageGenerator(self)

  async def periodic_attack(self):
    while self.monster_hp > 0:
        await asyncio.sleep(5)
        if self.monster_hp > 0:
            print("\n몬스터가 공격했다! 그러나 아무 일도 없었다.")

  async def fightprocess(self):
    for msg in self.msg_gen.initial_messages():
        print(msg)

    task = asyncio.create_task(self.periodic_attack())
    loop = asyncio.get_running_loop()

    while self.monster_hp > 0:
        for msg in self.msg_gen.turn_start_messages():
            print(msg)

        prompt = next(self.msg_gen.input_prompt_message())
        choice = await loop.run_in_executor(None, input, prompt)

        try:
            skill_name, damage = self.skills[choice]
        except KeyError:
            print("잘못된 입력입니다.")
            task.cancel()
            exit()

        self.monster_hp -= damage
        if self.monster_hp < 0:
          self.monster_hp = 0

        for msg in self.msg_gen.damage_report_message(damage):
            print(msg)

        if self.monster_hp > 0:
            for msg in self.msg_gen.counter_attack_message():
                print(msg)
        else:
            for msg in self.msg_gen.victory_message():
                print(msg)
            break
    
    task.cancel()

if __name__ == "__main__":
    game_instance = MonsterConquest()
    asyncio.run(game_instance.fightprocess())