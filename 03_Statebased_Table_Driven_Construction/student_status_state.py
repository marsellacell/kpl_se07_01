from enum import Enum

#state
class StudentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"
    
#Trigger Input
class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    
#Transition
state_transitions = {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR
    },
    StudentStatusState.AKTIF: {
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    }
}

def change_state(current_state, trigger_input):
    cond1 = current_state in state_transitions #Return True or False
    cond2 = trigger_input in state_transitions[current_state] #Return True or False
    if cond_1 and cond_2:
        #TERDAFTAR, AKTIF, LULUS, CUTI
        return state_transitions[current_state][trigger_input]
    return "Transisi Tidak Valid"

current_state = StudentStatusState.TERDAFTAR
Trigger_Input = TriggerInputState.CETAK_KSM

next_state = change_state(current_state, trigger_input)
print(next_state)