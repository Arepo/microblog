def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()



print('')




def decorator(new_func):
  def wrappy():
     print('sup dollface')
     new_func()
     print('buhbye')

  return wrappy

def chatty():
  print('why hi there')


my_func = decorator(chatty)

my_func()

@decorator
def natty():
  print('kiero')

natty()
