from abc import ABC , abstractmethod

class BaseAgent():

    def __init__(self, name:str,role:str,system_prompt:str):
        self.name=name
        self.role = role
        self.system_prompt = system_prompt
        
    
    def think(self,query:str) ->str:
        """
        Process the input query and return the agent's response.
        """
        pass