
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            
            {"id":3443,
            "first_name":"Tommy",
            "last_name":last_name,
            "age":33,
            "lucky_numbers":[7, 13, 22]
        },
           {
                "id":3443,
                "first_name":"Jane",
                "last_name":last_name,
                "age":35,
                "lucky_numbers":[10, 14, 3]
           },
             {
                "id":self._generateId(),
                "first_name":"Jimmy",
                "last_name":last_name,
                "age":5,
                "lucky_numbers":1
           }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
       self._members.append(member)
       return self._members
       

    def delete_member(self, id):
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)

        return{"done": True}
    

    def delete_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                self._members.remove(member)
                return{"done": "True"}
        return {"done": "False"}

    def update_member(self, id, member_id):
        self._members=[update_member if member["id"]== member_id else member for member in self._members ]
        return self._members


    def get_member(self, id):
        member_needed=next((member for member in self._members if member["id"]==id),None)
        return member_needed if member_needed else {}
            
        return False

    

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
