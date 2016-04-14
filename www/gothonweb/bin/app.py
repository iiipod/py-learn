import web

urls = (
        '/', 'Index'
        )

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        greeting = "Hello world"
#        return render.index(greeting = greeting)
        return render.foo(greeting = greeting)
if __name__ == "__main__":
    app.run()
