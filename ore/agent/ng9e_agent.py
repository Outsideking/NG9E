from planner import Planner
from executor import Executor
from memory import Memory
from core.language.htp_parser import HTPParser
from core.language.talksense import TalkSense

class NG9EAgent:
    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.memory = Memory()
        self.htp = HTPParser()
        self.talksense = TalkSense()

    def run(self, input_data):
        intent, confidence = self.htp.parse(input_data)
        emotion = self.talksense.analyze(input_data)
        tasks = self.planner.decompose(intent, input_data)
        results = [self.executor.execute(task) for task in tasks]
        self.memory.update(results)
        return results
