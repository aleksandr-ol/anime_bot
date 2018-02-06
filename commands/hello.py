import command_system


def hello():
   message = 'Что опять поговорить не с кем?Давай аниме чтоль посмотрим'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'Здорова', 'Говори', 'здравствуйте', 'дороу', 'hi']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello
