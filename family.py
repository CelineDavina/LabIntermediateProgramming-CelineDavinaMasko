
class Family:
  def __init__(self, children=[]):
    self.children = children

  def add_child(self, child):
    self.children.append(child)

  def remove_child(self, child):
    self.children.remove(child)

  def get_children(self):
    return self.children

  def __iter__(self):
    return iter(self.children)

  def __len__(self):
    return len(self.children)
  
