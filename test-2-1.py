from core.base import Base

class Test(Base):
    def initialize(self):
        print("initializing program....")
        print("loading....")
    
    def update(self):
        pass


Test().run()