import web

urls = (
        '/hello', 'Index'
        )

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

#class Index:
#    def GET(self):
#        greeting = "Hello World"
#        return render.index(greeting = greeting)
##        return render.foo(greeting = greeting)

class Index:
    def GET(self):
        form = web.input(name="Nobody")
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" %(form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
