
class CourtCase:
    def __init__(self, case_number):
        self.case_number = case_number
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""

    def set_a_listening_datetime(self, datetime):
        self.listening_datetimes.append(datetime)

    def add_participant(self, inn):
        if inn not in self.case_participants:
            self.case_participants.append(inn)

    def remove_participant(self, inn):
        if inn in self.case_participants:
            self.case_participants.remove(inn)

    def make_a_decision(self, verdict):
        self.verdict = verdict
        self.is_finished = True


# Пример
if __name__ == "__main__":
    case = CourtCase("А123-2025")

    case.add_participant("123456789012")
    case.add_participant("987654321098")
    case.set_a_listening_datetime("2025-10-20 14:00")
    case.set_a_listening_datetime("2025-10-25 10:00")
    case.remove_participant("123456789012")
    case.make_a_decision("Виновен")

    print(f"Номер дела: {case.case_number}")
    print(f"Участники: {case.case_participants}")
    print(f"Заседания: {case.listening_datetimes}")
    print(f"Завершено: {case.is_finished}")
    print(f"Решение: {case.verdict}")
