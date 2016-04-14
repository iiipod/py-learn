import web

urls = (
        '/', 'Index'
        )

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)
#        return render.foo(greeting = greeting)

class Form:
    def GET(self):
        greeting = "hello, Form"
        return render.hello_form(greeting = greeting)

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" %(form.greet, form.name)
        return render.hello_form(greeting = greeting)

if __name__ == "__main__":
    app.run()
