# Simple Python JSON Server

`watchgod request_handler.main`

## Deploying to Heroku

1. Create an account on [Heroku](https://heroku.com/), It's free.
1. At the dashboard, click the New button and select "Create a new app". Give the app whatever name you like.
1. [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
1. Login to Heroku with `heroku login`.
1. Add `Procfile` to project with the following content.
    ```
    web: python request_handler.py $PORT
    ```
1. Change end of request handler to the following code.
    ```py
    def main():
        host = ''
        port = int(os.environ['PORT'])
        HTTPServer((host, port), HandleRequests).serve_forever()


    main()
    ```
1. Remove `.db` from your `.gitignore` file.
1. `heroku git:remote -a kennel-server`
1. `git push heroku main` and wait for the deploy to complete.
1. Activate dyno with `heroku ps:scale web=1` and wait for confirmation that it started.
1. Open Postman and perform a GET to your deployed app's URL and a resource and you should get a response.

