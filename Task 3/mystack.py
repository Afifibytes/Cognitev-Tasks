class mystack():
     def __init__(self):
         self.items = []

     def add_item(self, item1, item2 = None):
          if item2 == None:
               self.items.append(item1)
          else:
               self.items.append(item1)
               self.items.append(item2)

     def pop_item(self):
          if not self.items == []:
               return self.items.pop()

     def count_items(self):
         return len(self.items)

