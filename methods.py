# Methods

# class MethodExamples:
#
#     def __init__(self):
#      self.this_can_be_accessed_easily = "Hi, I am easily found!"
    # this_can_be_accessed_easily = "Hi, I am easily found"

#     this_can_be_accessed_easily ="Hi, I am easily found"
#
# x = MethodExamples()
# #
# print(x.this_can_be_accessed_easily)
# x.this_can_be_accessed_easily ="Hi, I am easily found"
# print(x.this_can_be_accessed_easily) # we don't want our class variables to be accessible

class MethodExamples:
    def __init__(self):
        self._this_can_be_accessed_easily + "Hi, here I am easily found" #for variable, method is double underscore

    # this_can_be_accessed_easily = "Hi, here I am easily found"

x = MethodExamples()

print(x._this_can_be_accessed_easily)
x.set_this_can_be_accessed_easily = "I have been changed"
print(x._this_can_be_accessed_easily)  # we don't want our class variables to be accessible
 # more secure. private

