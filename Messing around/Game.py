import random
used_ids = []

class life_form:
    def __init__(self,name, temp_id=random.randint(1,500), life_span=120, age=0, race='N/A', bloodlines = {}, providence = 0, cultivation_stage = 'None', drahma = {}, mystical_powers = {}):
        self.name = name
        self.life_span = {
            'age' : age,
            'span' : life_span
            }
        self.user_id = temp_id
        while True:
            if self.user_id not in used_ids:
                used_ids.append(self.user_id)
                break
            else:
                self.user_id = random.randint(1,500)
        self.race = race
        self.providence = providence
        self.cultivation_stage = cultivation_stage
        # Name : effects
        self.bloodlines = bloodlines
        self.drahma = drahma
        self.mystical_powers = mystical_powers
             
                
